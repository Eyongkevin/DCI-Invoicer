from typing import Tuple

from apps.core.abstracts import AbstractSerializer

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
        read_only_fields: Tuple[str, ...] = ("is_active", "created", "updated")
