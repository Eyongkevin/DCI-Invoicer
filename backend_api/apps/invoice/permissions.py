from typing import Dict

from rest_framework.permissions import BasePermission


class UserIDBelongToUser(BasePermission):
    message: Dict[str, str] = {
        "detail": "Can't perform action for another user",
        "code": "not_user_failed",
    }

    def has_object_permission(self, request, view, obj) -> bool:
        return request.data.get("user_id") == str(request.user.public_id)

    def has_permission(self, request, view) -> bool:
        return True
