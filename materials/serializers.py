from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"


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

    # def get_lessons(self, course):
    #     """возвращает lessons - все уроки в курсе"""
    #     return [lesson.title for lesson in Lesson.objects.filter(course=course)]
