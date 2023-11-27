import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError) as err:
            raise Http404 from err


class AbstractUserManager(AbstractManager):
    def get_object_by_user_id(self, user_id):
        try:
            breakpoint()
            instance = self.get(user_id__public_id=user_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError) as err:
            raise Http404 from err


class AbstractModel(models.Model):
    public_id = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = AbstractManager()

    class Meta:
        abstract = True


# class AbstractUserModel(AbstractModel):
#     user_id = models.OneToOneField("apps_user.User", on_delete=models.CASCADE)

#     class Meta:
#         abstract = True
