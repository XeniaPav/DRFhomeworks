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

    def get_lessons_count(self, obj):
        """возвращает lessons_count - количество уроков в курсе"""
        if obj.lesson_set.all().count():
            return obj.lesson_set.all().count()
        else:
            return 0

    def get_lessons(self, course):
        """возвращает lessons - все уроки в курсе"""
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"