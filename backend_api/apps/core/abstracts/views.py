from rest_framework.viewsets import ModelViewSet


class AbstractViewSet(ModelViewSet):
    lookup_field = "public_id"
    ordering_fields = ("updated", "created")
    ordering = ("-updated",)
