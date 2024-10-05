from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    """Сериалайзер для платежей"""
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериалайзер для пользователей"""
    class Meta:
        model = User
        fields = "__all__"

