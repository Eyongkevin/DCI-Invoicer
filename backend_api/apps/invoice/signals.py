from django.db import models
from django.dispatch import receiver

from .models import Invoice


@receiver(models.signals.post_delete, sender=Invoice)
def delete_file_on_s3(sender, instance, **kwargs):
    if instance.invoice_xls:
        instance.invoice_xls.delete(save=False)
    if instance.invoice_pdf:
        instance.invoice_pdf.delete(save=False)
