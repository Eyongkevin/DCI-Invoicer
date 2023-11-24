from apps.core.abstracts import AbstractViewSet
from apps.core.permissions import OnlyAdminAndSuperuserPermission, UserPermission

from .models import User
from .serializers import UserSerializer


class UserViewSet(AbstractViewSet):
    http_method_names = ("get",)
    permission_classes = (UserPermission, OnlyAdminAndSuperuserPermission)
    serializer_class = UserSerializer
    filterset_fields = ("role", "is_active")
    queryset = User.objects.all()
