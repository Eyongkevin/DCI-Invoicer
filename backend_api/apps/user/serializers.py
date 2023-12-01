from typing import Dict, NoReturn, Tuple, Union

from apps.core.abstracts import AbstractSerializer
from apps.core.exceptions import UserMismatchPasswordsEx
from apps.core.schemas import UserRoleEnum
from rest_framework import serializers

from .models import Address, Assignment, Company, Profile, User


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


class ProfileSerializer(AbstractSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    class Meta:
        model: Profile = Profile
        fields = (
            "id",
            "user_id",
            "tax_number",
            "po_number",
            "vat_id",
            "bank_name",
            "iban",
            "first_name",
            "last_name",
            "swift_bic",
            "class_room",
            "transfer_deadline_day",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")


class AddressSerializer(AbstractSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    class Meta:
        model: Address = Address
        fields = (
            "id",
            "user_id",
            "po_box",
            "city",
            "country",
            "address",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")


class CompanySerializer(AbstractSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    class Meta:
        model: Company = Company
        fields = (
            "id",
            "user_id",
            "name",
            "address_1",
            "address_2",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")


class AssignmentSerializer(AbstractSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    class Meta:
        model: Assignment = Assignment
        fields = (
            "id",
            "user_id",
            "signed_agreement",
            "end_date",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")
