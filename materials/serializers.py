from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="url")]


class CourseSerializer(serializers.ModelSerializer):
    """Сериалайзер для курса"""

    class Meta:
        model = Course
        fields = "__all__"

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    def get_lessons_count(self, obj):
        """возвращает lessons_count - количество уроков в курсе"""
        if obj.lesson_set.all().count():
            return obj.lesson_set.all().count()
        else:
            return 0


class SubscriptionSerializer(ModelSerializer):
    """Сериалайзер для подписок"""

    class Meta:
        model = Subscription
        fields = "__all__"
