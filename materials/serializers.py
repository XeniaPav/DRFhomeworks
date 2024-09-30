from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериалайзер для курса"""

    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lessons_count(obj):
        """возвращает lessons_count - количество уроков в курсе"""
        return Lesson.objects.filter(course=obj.pk).count()


class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"

    def get_lessons(obj):
        """возвращает lessons - все уроки в курсе"""
        return [lesson.title for lesson in Lesson.objects.filter(course=obj.pk)]