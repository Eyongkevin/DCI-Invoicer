from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response


class InsertUserIdMixins:
    def get_queryset(self):
        breakpoint()
        # return super().get_queryset()


class FilterByLoggedUserMixin:
    def get_queryset(self):
        profiles = super().get_queryset()
        public_id = str(self.request.user.public_id)
        return profiles.filter(user_id__public_id=public_id)


class CreateMixin:
    def create(self, request, *args, **kwargs):
        user_id = request.user.public_id
        data = request.data
        data.update({"user_id": user_id})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError as err:
            return Response(
                {
                    "detail": "User profile already exist",
                    "code": "user_duplicate_error",
                },
                status=status.HTTP_409_CONFLICT,
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
