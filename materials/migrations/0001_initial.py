# Generated by Django 5.1.1 on 2024-09-30 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=50,
                        verbose_name="Название",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью курса",
                        null=True,
                        upload_to="materials/preview/",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание курса",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=50,
                        verbose_name="Название",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью урока",
                        null=True,
                        upload_to="materials/preview/",
                        verbose_name="превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание урока",
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="Введите ссылку на видео урока",
                        max_length=100,
                        verbose_name="Ссылка на урок",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="Укажите курс урока",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
