import uuid
import os
from django.db import models
from django.contrib.auth import get_user_model
import jsonfield
from django.utils.translation import gettext as _

from utils import GeneralModel

User = get_user_model()


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/post/', filename)


class Patient(GeneralModel):
    creator = models.ForeignKey(
        User,
        verbose_name=_('Patient Creator'),
        on_delete=models.CASCADE,
        related_name='patient'
    )
    first_name = models.CharField(
        max_length=300,
    )
    last_name = models.CharField(
        max_length=300,
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    id_code = models.BigIntegerField()
    city = models.CharField(
        max_length=300
    )
    phone = models.BigIntegerField()
    state = jsonfield.JSONField(
        null=True,
        blank=True
    )

    def __str__(self):
        f'{self.first_name} {self.last_name} | {self.creator}'