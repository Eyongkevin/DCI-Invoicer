import secrets

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.core.abstracts import AbstractSerializer
from apps.user.models import User

from .models import Invoice


class InvoiceSerializer(AbstractSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    def create(self, validated_data):
        try:
            file = validated_data["invoice_xls"]
            name, _, ext = file.name.rpartition(".")
            name = f"{name}_{secrets.token_urlsafe(10)}.{ext}"
            validated_data["invoice_xls"].name = name

            return super().create(validated_data)
        except (ValueError, IndexError) as err:
            raise ValidationError(
                {
                    "detail": "uploaded document couldn't be processed",
                    "code": "invalid_upload_doc_failed",
                }
            )

    class Meta:
        model = Invoice
        fields = (
            "id",
            "user_id",
            "name",
            "size",
            "invoice_xls",
            "invoice_pdf",
            "created",
            "updated",
        )
        read_only_fields = ("created", "updated")
