import pytest
from apps.core.fixtures import user
from apps.user.models import Profile

data_profile = {
    "tax_number": "P079017863310R",
    "po_number": "PO-598",
    "vat_id": None,
    "bank_name": "UBA Cameroon SA",
    "iban": "CM21 10033 05212 12002006853 24",
    "swift_bic": "UNAFCMCX",
    "first_name": "kevin Enowanyo",
    "last_name": "Eyong",
    "transfer_deadline_day": 16,
}


@pytest.mark.django_db
def test_create_profile(user):
    data_profile["user_id"] = user

    profile = Profile.objects.create(**data_profile)

    assert profile.user_id.public_id.hex == user.public_id.hex
    assert data_profile["tax_number"] == profile.tax_number
    assert str(profile) == f"{data_profile['last_name']} {data_profile['first_name']}"
