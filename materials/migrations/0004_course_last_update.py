# Generated by Django 5.1.1 on 2024-10-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="last_update",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Последнее обновление"
            ),
        ),
    ]
