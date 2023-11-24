from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/auth/login", views.LoginViewSet, basename="v1-auth-login")
router.register(r"v1/auth/register", views.RegisterViewSet, basename="v1-auth-register")
router.register(
    r"v1/auth/refresh-token", views.RefreshViewSet, basename="v1-auth-refresh-token"
)
urlpatterns = [
    *router.urls,
]
