from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/invoice", views.InvoiceViewSet, basename="v1-invoice")


urlpatterns = [
    path(
        "v1/invoice/<public_id>/generate/",
        views.pdf_generate,
        name="v1-generate-invoice",
    ),
    *router.urls,
]
