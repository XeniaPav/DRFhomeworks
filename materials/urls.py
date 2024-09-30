from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import SimpleRouter

from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register("course", CourseViewSet)

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path("lesson/delet/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delet"),
]

urlpatterns += router.urls
