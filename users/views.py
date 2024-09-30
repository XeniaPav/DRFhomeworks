from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payment
from users.serializers import PaymentSerializer


class UserViewSet(ModelViewSet):
    """вьюсет для модели пользователя"""
    queryset = User.objects.all()

class PaymentListAPIView(ListAPIView):
    """контроллер для списка платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['pay_date']
