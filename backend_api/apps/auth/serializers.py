import re
from typing import Any, Dict, NoReturn, Tuple, Union

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import Token

from apps.core.exceptions import UserNonDCIFreelancerEmailEx
from apps.core.schemas import UserRoleEnum
from apps.user.models import User
from apps.user.serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data: Dict = super().validate(attrs)
        refresh: Token = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class RegistrationSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model: User = User
        fields: Tuple[str] = (
            "id",
            "username",
            "email",
            "role",
            "password",
        )

    def validate(self, data) -> Union[str, NoReturn]:
        email: str = data.get("email")
        if not re.search(
            r"^[a-zA-Z0-9.\-]{10,50}freelancer@digitalcareerinstitute.org$", email
        ):
            raise UserNonDCIFreelancerEmailEx()
        return data

    def create(self, validated_data) -> Union[User, NoReturn]:
        validated_data["role"] = UserRoleEnum(validated_data.get("role"))
        return User.objects.create_user(**validated_data)
