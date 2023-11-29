from django.db import models

from apps.core.abstracts import AbstractModel, AbstractUserManager

from .validators import validate_file_extension


# Create your models here.
class InvoiceManager(AbstractUserManager):
    ...


class Invoice(AbstractModel):
    user_id = models.ForeignKey(
        "apps_user.User", on_delete=models.CASCADE, related_name="invoice"
    )
    size = models.PositiveSmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    invoice_xls = models.FileField(max_length=50, validators=[validate_file_extension])
    invoice_pdf = models.URLField(null=True, blank=True)
