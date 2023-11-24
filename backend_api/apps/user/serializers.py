from typing import NoReturn, Tuple, Union

from apps.core.abstracts import AbstractSerializer
from apps.core.schemas import UserRoleEnum

from .models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model: User = User
        fields: Tuple[str, ...] = (
            "id",
            "username",
            "email",
            "role",
            "is_active",
            "created",
            "updated",
        )
        read_only_fields: Tuple[str, ...] = ("created", "updated")

    def update(self, instance, validated_data):
        if validated_data.get("role") == UserRoleEnum.superuser.value:
            instance.is_superuser = True
        else:
            isinstance.is_superuser = False
        return super().update(instance, validated_data)
