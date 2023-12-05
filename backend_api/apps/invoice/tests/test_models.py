import os
import re

import mock
import pytest
from apps.core.fixtures import user
from apps.invoice.models import Invoice
from django.core.files import File

data_invoice = {
    "name": "November 2023 invoice",
}


@pytest.mark.django_db
def test_create_invoice(user):
    data_invoice["user_id"] = user
    file_mock = mock.MagicMock(spec=File)
    file_mock.name = "november_2023_invoice.xlsx"
    data_invoice["invoice_xls"] = file_mock

    invoice = Invoice.objects.create(**data_invoice)

    file_name = invoice.invoice_xls.file.name.rpartition(os.path.sep)[-1]

    assert re.search(r"november_2023_invoice_[\w]{7}.xlsx", file_name) is not None
