from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/auth/login", views.LoginViewSet, basename="v1-auth-login")

urlpatterns = [
    *router.urls,
]
