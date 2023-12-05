import pytest
from apps.core.fixtures import user
from apps.user.models import Company

data_company = {
    "name": "DCI-Digital Career Institute GmbH",
    "address_1": "Vulkanstr. 1",
    "address_2": "10367 Berlin",
}


@pytest.mark.django_db
def test_create_company(user):
    data_company["user_id"] = user

    company = Company.objects.create(**data_company)

    assert company.user_id.public_id.hex == user.public_id.hex
    assert company.address_1 == data_company["address_1"]
    assert str(company) == data_company["name"]
