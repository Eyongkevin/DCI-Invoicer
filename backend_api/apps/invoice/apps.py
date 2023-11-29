from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvoiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.invoice"
    label = "apps_invoice"
    verbose_name = _("Invoice")
