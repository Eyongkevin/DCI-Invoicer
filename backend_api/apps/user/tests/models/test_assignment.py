import pytest
from apps.core.fixtures import user
from apps.user.models import Assignment

data_assignment = {"signed_agreement": "2023-11-15", "end_date": "2024-11-15"}


@pytest.mark.django_db
def test_create_assignment(user):
    data_assignment["user_id"] = user

    assignment = Assignment.objects.create(**data_assignment)

    assert assignment.user_id.public_id.hex == user.public_id.hex
    assert assignment.end_date == data_assignment["end_date"]
    assert str(assignment) == f"{user.username} - {data_assignment['end_date']}"
