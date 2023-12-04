import pytest
from apps.core.fixtures import user
from apps.core.schemas import UserRoleEnum
from django.contrib.auth import get_user_model
from django.http import Http404

data_user = {
    "username": "kevin",
    "email": "kevin.kenz-freelancer@digitalcareerinstitute.org",
    "password": "kevin@2023",
    "role": UserRoleEnum("US"),
}


class TestUserManager:
    @pytest.mark.django_db
    def test_create_user(self):
        user = get_user_model().objects.create_user(**data_user)
        assert user.username == data_user["username"]
        assert user.email == data_user["email"]
        assert user.role == data_user["role"].value
        assert user.is_superuser == False
        assert user.is_staff == False

    @pytest.mark.django_db
    def test_create_superuser(self):
        data_user["role"] = UserRoleEnum("SU")

        user = get_user_model().objects.create_superuser(**data_user)
        assert user.username == data_user["username"]
        assert user.email == data_user["email"]
        assert user.role == data_user["role"].value
        assert user.is_superuser == True
        assert user.is_staff == True

    @pytest.mark.django_db
    def test_invalid_role(self):
        data_user["role"] = "SU"

        with pytest.raises(TypeError) as ex:
            get_user_model().objects.create_user(**data_user)
        assert ex.value.args[0] == "User role must be of the instance 'UserRoleEnum'"

    @pytest.mark.django_db
    def test_invalid_role_for_superuser(self):
        with pytest.raises(TypeError) as ex:
            get_user_model().objects.create_superuser(**data_user)
        assert ex.value.args[0] == "Superuser must have role set to 'superuser'"

    @pytest.mark.django_db
    def test_get_object_by_username(self, user):
        a_user = get_user_model().objects.get_object_by_username(username=user.username)
        assert isinstance(a_user, get_user_model())
        assert a_user.username == user.username

    @pytest.mark.django_db
    def test_get_object_by_username_fail(self):
        with pytest.raises(Http404) as err:
            get_user_model().objects.get_object_by_username(username="kevin")
