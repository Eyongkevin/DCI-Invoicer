import pytest
from apps.core.schemas import UserRoleEnum
from django.contrib.auth import get_user_model

data_user = {
    "username": "kevin",
    "email": "kevin.kenz-freelancer@digitalcareerinstitute.org",
    "password": "kevin@2023",
    "role": UserRoleEnum("US"),
}


@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(**data_user)


@pytest.fixture
def admin(db):
    data_user["username"] = "enow"
    data_user["email"] = "admin-freelancer@digitalcareerinstitute.org"
    data_user["role"] = UserRoleEnum("AD")
    return get_user_model().objects.create_user(**data_user)


@pytest.fixture
def superuser(db):
    data_user["username"] = "eyong"
    data_user["email"] = "eyong-freelancer@digitalcareerinstitute.org"
    data_user["role"] = UserRoleEnum("SU")
    return get_user_model().objects.create_superuser(**data_user)
