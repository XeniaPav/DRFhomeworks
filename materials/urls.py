from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import SimpleRouter

from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    SubscriptionCreateAPIView,
)

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register("course", CourseViewSet)

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-view"),
    path(
        "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path(
        "lesson/<int:pk>/destroy/",
        LessonDestroyAPIView.as_view(),
        name="lesson-destroy",
    ),
    path("subscription/create/", SubscriptionCreateAPIView.as_view(), name="subscribe"),
]

urlpatterns += router.urls
