from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(request.user and request.user.is_authenticated)

    def has_permission(self, request, view) -> bool:
        return bool(request.user and request.user.is_authenticated)
