from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/users", views.UserViewSet, basename="v1-users")

urlpatterns = [
    *router.urls,
]
