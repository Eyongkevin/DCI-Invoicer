from typing import Dict

from rest_framework.permissions import BasePermission

from apps.core.schemas import UserRoleEnum


class UpdateRoleToSuperuserNotAllowed(BasePermission):
    message: Dict[str, str] = {
        "detail": "Can't update role to Superuser",
        "code": "role_update_failed",
    }

    def has_object_permission(self, request, view, obj) -> bool:
        return not bool(request.data.get("role") == UserRoleEnum.superuser.value)

    def has_permission(self, request, view) -> bool:
        return True


class UpdateSuperuserRoleNotAllowed(BasePermission):
    message: Dict[str, str] = {
        "detail": "Role of Superuser can't be updated",
        "code": "role_update_failed",
    }

    def has_object_permission(self, request, view, obj) -> bool:
        return not obj.is_superuser

    def has_permission(self, request, view) -> bool:
        return True
