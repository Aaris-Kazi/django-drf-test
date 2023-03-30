from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("studentapi", views.StudentViewSet, basename="student")

urlpatterns = [
    path("", include(router.urls))
]
