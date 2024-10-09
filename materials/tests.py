from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@ad.com", password="admin")
        self.course = Course.objects.create(title="test", owner=self.user)
        self.lesson = Lesson.objects.create(
            title="test_les", course=self.course, url="url", owner=self.user
        )
        self.subscription = Subscription.objects.create(
            course=self.course, user=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-view", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "test_les")

    def test_lesson_create(self):
        url = reverse("materials:lesson-create")
        data = {
            "title": "lesson_test",
            "course": self.course.pk,
            "url": "https://www.youtube.com/watch?v=SuJCgGhN_SU",
            "owner": self.user.pk,
        }
        data1 = {
            "title": "lesson_test",
            "course": self.course.pk,
            "url": "https://www.video.com/watch?v=SuJCgGhN_SU",
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        response1 = self.client.post(url, data1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "lesson_test_new",
            "course": self.course.pk,
            "url": "https://www.youtube.com/watch?v=SuJCgGhN_SU",
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "lesson_test_new")

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "title": "test_les",
                        "preview": None,
                        "description": None,
                        "url": "url",
                        "course": self.lesson.course.pk,
                        "owner": self.user.pk,
                    }
                ],
            },
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson-destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Course Description",
        )
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test Lesson Description",
            course=self.course,
        )
        self.url = reverse("materials:subscribe")

    def test_subscriptions_create(self):
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscriptions_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
