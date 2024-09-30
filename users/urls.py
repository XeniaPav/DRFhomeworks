from django.urls import path
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView
from rest_framework.routers import SimpleRouter


app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)


urlpatterns = [
    path("payment_list/", PaymentListAPIView.as_view(), name="payment_list"),
]

urlpatterns += router.urls
