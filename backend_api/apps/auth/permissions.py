from typing import Dict

from rest_framework.permissions import BasePermission

from apps.core.schemas import UserRoleEnum


class RegistrationOnlyAdminAndSuperuserPermission(BasePermission):
    message: Dict[str, str] = {
        "detail": "Only Admin and Superuser can perform registration",
        "code": "registration_only_admin_or_superuser_failed",
    }

    def _is_admin_or_superuser(self, request) -> bool:
        if request.user:
            return bool(
                request.user.is_superuser
                or request.user.role == UserRoleEnum.admin.value
            )
        return False

    def has_object_permission(self, request, view, obj) -> bool:
        if self._is_admin_or_superuser(request):
            return True
        return False

    def has_permission(self, request, view) -> bool:
        if self._is_admin_or_superuser(request):
            return True
        return False


class OnlySuperuserCreateSuperuserPermission(BasePermission):
    message: Dict[str, str] = {
        "detail": "Only a superuser can create another superuser",
        "code": "only_superuser_create_superuser_failed",
    }

    def has_permission(self, request, view) -> bool:
        if request.data.get("role") == UserRoleEnum.superuser.value:
            return request.user.is_superuser
        return True
