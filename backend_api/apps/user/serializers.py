from apps.core.abstracts import AbstractSerializer

from .models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
            "is_active",
            "created",
            "updated",
        )
        read_only_fields = ("is_active", "created", "updated")
