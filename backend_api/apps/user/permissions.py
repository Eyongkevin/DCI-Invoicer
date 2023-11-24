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
        if request.method == "PATCH":
            return not obj.is_superuser
        return True

    def has_permission(self, request, view) -> bool:
        return True


class DeleteSuperuserNotAllowed(BasePermission):
    message: Dict[str, str] = {
        "detail": "Superuser can't be deleted",
        "code": "delete_superuser_failed",
    }

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method == "DELETE":
            return not obj.is_superuser
        return True

    def has_permission(self, request, view) -> bool:
        return True
