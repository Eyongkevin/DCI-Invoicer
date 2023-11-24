from typing import Dict, NoReturn, Tuple, Union

from rest_framework import serializers

from apps.core.abstracts import AbstractSerializer
from apps.core.exceptions import UserMismatchPasswordsEx
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
            instance.is_superuser = False
        return super().update(instance, validated_data)


class ResetPasswordSerializer(AbstractSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
    cpassword = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    def validate(self, data) -> Union[Dict[str, str], NoReturn]:
        if data.get("password") != data.get("cpassword"):
            raise UserMismatchPasswordsEx()
        return data

    #! set the password here will properly hash the password
    def save(self, **kwargs) -> User:
        password: str = self.validated_data["password"]
        user: User = self.instance
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model: User = User
        fields = ("password", "cpassword")
