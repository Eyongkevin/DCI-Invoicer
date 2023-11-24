from typing import Dict

from rest_framework.permissions import BasePermission

from apps.core.schemas import UserRoleEnum


class OnlySuperuserCreateSuperuserPermission(BasePermission):
    message: Dict[str, str] = {
        "detail": "Only a superuser can create another superuser",
        "code": "only_superuser_create_superuser_failed",
    }

    def has_permission(self, request, view) -> bool:
        if request.data.get("role") == UserRoleEnum.superuser.value:
            return request.user.is_superuser
        return True
