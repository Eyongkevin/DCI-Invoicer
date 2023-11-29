from django.apps import AppConfig
from django.core.signals import request_finished
from django.utils.translation import gettext_lazy as _


class InvoiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.invoice"
    label = "apps_invoice"
    verbose_name = _("Invoice")

    def ready(self) -> None:
        from . import signals

        request_finished.connect(signals.delete_file_on_s3)
