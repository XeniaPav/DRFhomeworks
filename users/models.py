from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson, NULLABLE
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите e-mail"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )

    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Ведите город",
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель платежа"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )
    pay_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    price = models.PositiveIntegerField(verbose_name="Оплаченная сумма")
    CASH = "Наличные"
    TRANSFER = "Перевод"
    methods = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]
    method = models.CharField(max_length=8, choices=methods, default=TRANSFER)

    def __str__(self):
        return f"{self.price}р. - {self.pay_date}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
