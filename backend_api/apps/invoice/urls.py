from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"v1/invoice", views.InvoiceViewSet, basename="v1-invoice")


urlpatterns = [
    *router.urls,
]
