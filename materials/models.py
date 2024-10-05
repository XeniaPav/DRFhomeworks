from config import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название курса"
    )
    preview = models.ImageField(
        upload_to="materials/preview/",
        verbose_name="Превью",
        **NULLABLE,
        help_text="Загрузите превью курса",
    )
    description = models.TextField(
        verbose_name="Описание", **NULLABLE, help_text="Введите описание курса"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        help_text="Укажите владельца курса",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название урока"
    )
    preview = models.ImageField(
        upload_to="materials/preview/",
        verbose_name="превью",
        **NULLABLE,
        help_text="Загрузите превью урока",
    )
    description = models.TextField(
        verbose_name="Описание", **NULLABLE, help_text="Введите описание урока"
    )
    url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на урок",
        help_text="Введите ссылку на видео урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс урока",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        help_text="Укажите владельца урока",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
