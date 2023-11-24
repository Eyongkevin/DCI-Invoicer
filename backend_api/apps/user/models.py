from typing import NoReturn, Union

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.abstracts import AbstractManager, AbstractModel
from apps.core.schemas import UserRoleEnum

# Create your models here.


class UserManager(BaseUserManager, AbstractManager):
    def create_user(
        self,
        username: str,
        email: str,
        role: UserRoleEnum = UserRoleEnum("US"),
        password: str = None,
        **kwargs
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
