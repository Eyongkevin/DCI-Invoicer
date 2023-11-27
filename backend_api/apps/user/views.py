from rest_framework.response import Response

from apps.core.abstracts import AbstractViewSet
from apps.core.exceptions import UserMismatchPasswordsEx, UserMissingCpasswordEx
from apps.core.permissions import OnlyAdminAndSuperuserPermission, UserPermission

from .mixins import CreateMixin, FilterByLoggedUserMixin, InsertUserIdMixins
from .models import Address, Assignment, Company, Profile, User
from .permissions import (
    DeleteSuperuserNotAllowed,
    ObjectBelongToUser,
    UpdateRoleToSuperuserNotAllowed,
    UpdateSuperuserRoleAllowed,
)
from .serializers import (
    AddressSerializer,
    AssignmentSerializer,
    CompanySerializer,
    ProfileSerializer,
    ResetPasswordSerializer,
    UserSerializer,
)


class UserViewSet(AbstractViewSet):
    http_method_names = ("get", "patch", "delete")
    permission_classes = (
        UserPermission,
        OnlyAdminAndSuperuserPermission,
        UpdateRoleToSuperuserNotAllowed,
        UpdateSuperuserRoleAllowed,
        DeleteSuperuserNotAllowed,
    )
    serializer_class = UserSerializer
    filterset_fields = ("role", "is_active")
    queryset = User.objects.all()


class UserResetPassword(AbstractViewSet):
    http_method_names = ("patch",)
    permission_classes = (
        UserPermission,
        OnlyAdminAndSuperuserPermission,
        UpdateSuperuserRoleAllowed,
    )
    serializer_class = ResetPasswordSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs) -> Response:
        serializer: ResetPasswordSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        super().update(request, *args, **kwargs)

        return Response(
            {
                "detail": "User's password updated successfully",
                "code": "password_updated",
            }
        )


class ProfileViewSet(FilterByLoggedUserMixin, CreateMixin, AbstractViewSet):
    http_method_names = ("post", "get", "patch", "delete")
    permission_classes = (UserPermission, ObjectBelongToUser)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class AddressViewSet(FilterByLoggedUserMixin, CreateMixin, AbstractViewSet):
    http_method_names = ("post", "get", "patch", "delete")
    permission_classes = (UserPermission, ObjectBelongToUser)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class CompanyViewSet(FilterByLoggedUserMixin, CreateMixin, AbstractViewSet):
    http_method_names = ("post", "get", "patch", "delete")
    permission_classes = (UserPermission, ObjectBelongToUser)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class AssignmentViewSet(FilterByLoggedUserMixin, CreateMixin, AbstractViewSet):
    http_method_names = ("post", "get", "patch", "delete")
    permission_classes = (UserPermission, ObjectBelongToUser)
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
