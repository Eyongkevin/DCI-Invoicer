from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.abstracts import AbstractViewSet
from apps.core.permissions import UserPermission

from .models import Invoice
from .permissions import UserIDBelongToUser
from .serializers import InvoiceSerializer

# Create your views here.


class InvoiceViewSet(AbstractViewSet):
    http_method_names = ("post",)
    permission_classes = (UserPermission, UserIDBelongToUser)
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    @action(methods=["post"], detail=False)
    def upload(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
