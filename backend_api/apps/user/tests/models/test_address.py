import pytest
from apps.core.fixtures import user
from apps.user.models import Address

data_address = {
    "po_box": "00000",
    "city": "Yaounde",
    "country": "Cameroon",
    "address": "Biyem-Assi Junction",
}


@pytest.mark.django_db
def test_create_address(user):
    data_address["user_id"] = user

    address = Address.objects.create(**data_address)

    assert address.user_id.public_id.hex == user.public_id.hex
    assert address.address == data_address["address"]
    assert str(address) == user.username
