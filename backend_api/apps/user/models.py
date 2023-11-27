from typing import NoReturn, Union

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from apps.core.abstracts import AbstractManager, AbstractModel, AbstractUserManager
from apps.core.schemas import UserRoleEnum

# Create your models here.


class UserManager(BaseUserManager, AbstractManager):
    def create_user(
        self,
        username: str,
        email: str,
        role: UserRoleEnum = UserRoleEnum("US"),
        password: str = None,
        **kwargs,
    ) -> Union["User", NoReturn]:
        if username is None:
            raise TypeError("User must have a username")
        if email is None:
            raise TypeError("User must have an email")
        if password is None:
            raise TypeError("User must have a password")
        try:
            if not role in UserRoleEnum:
                raise ValueError(
                    "User must have a valid role: 'user', 'admin', 'superuser'"
                )
        except TypeError as err:
            raise TypeError("User role must be of the instance 'UserRoleEnum'") from err

        user: User = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role.value,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username: str, email: str, password: str, **kwargs
    ) -> Union["User", NoReturn]:
        if "role" in kwargs:
            if not kwargs.get("role") == UserRoleEnum.superuser:
                raise TypeError("Superuser must have role set to 'superuser'")
        else:
            kwargs["role"]: UserRoleEnum = UserRoleEnum("SU")

        user: User = self.create_user(
            username=username,
            email=email,
            password=password,
            **kwargs,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_object_by_username(self, username):
        try:
            instance = self.get(username=username)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError) as err:
            raise Http404 from err


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    class UserRole(models.TextChoices):
        USER = UserRoleEnum.user.value, _(UserRoleEnum.user.name.capitalize())
        ADMIN = UserRoleEnum.admin.value, _(UserRoleEnum.admin.name.capitalize())
        SUPERUSER = UserRoleEnum.superuser.value, _(
            UserRoleEnum.superuser.name.capitalize()
        )

    role = models.CharField(
        max_length=2,
        choices=UserRole.choices,
        default=UserRole.USER,
        db_index=True,
    )
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()


class ProfileManage(AbstractUserManager):
    ...


class Profile(AbstractModel):
    user_id = models.OneToOneField(
        "apps_user.User", on_delete=models.CASCADE, related_name="profile"
    )
    tax_number = models.CharField(50, null=True, blank=True)
    po_number = models.CharField(5, null=True, blank=True)
    vat_id = models.CharField(50, null=True, blank=True)
    bank_name = models.CharField(200, null=True, blank=True)
    iban = models.CharField(200, null=True, blank=True)
    swift_bic = models.CharField(200, null=True, blank=True)
    first_name = models.CharField(50, null=True, blank=True)
    last_name = models.CharField(50, null=True, blank=True)
    transfer_deadline_day = models.PositiveSmallIntegerField(null=True, blank=True)

    objects = ProfileManage()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class AddressManager(AbstractUserManager):
    ...


class Address(AbstractModel):
    user_id = models.OneToOneField(
        "apps_user.User", on_delete=models.CASCADE, related_name="address"
    )
    po_box = models.CharField(5, default="00000")
    city = models.CharField(50)
    country = models.CharField(100)
    address = models.CharField(150)

    def __str__(self) -> str:
        return self.user_id.username


class CompanyManager(AbstractUserManager):
    ...


class Company(AbstractModel):
    user_id = models.OneToOneField(
        "apps_user.User", on_delete=models.CASCADE, related_name="company"
    )
    name = models.CharField(100)
    address_1 = models.CharField(100)
    address_2 = models.CharField(100)

    def __str__(self):
        return self.name
