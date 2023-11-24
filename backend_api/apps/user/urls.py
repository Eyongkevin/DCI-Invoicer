from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/users", views.UserViewSet, basename="v1-users")
router.register(
    r"v1/users/reset-pwd", views.UserResetPassword, basename="v1-users-reset-pwd"
)


urlpatterns = [
    *router.urls,
]
