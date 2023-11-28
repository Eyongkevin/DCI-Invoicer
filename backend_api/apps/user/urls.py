from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/users", views.UserViewSet, basename="v1-users")
router.register(
    r"v1/users/reset-pwd", views.UserResetPassword, basename="v1-users-reset-pwd"
)
router.register(r"v1/user/profile", views.ProfileViewSet, basename="v1-user-profile")

router.register(r"v1/user/address", views.AddressViewSet, basename="v1-user-address")
router.register(r"v1/user/company", views.CompanyViewSet, basename="v1-user-company")
router.register(
    r"v1/user/assignment", views.AssignmentViewSet, basename="v1-user-assignment"
)

urlpatterns = [
    *router.urls,
]
