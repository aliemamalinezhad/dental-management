import uuid
import os
from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
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
    file = models.FileField(
        upload_to='patient/',
        blank=True,
        null=True
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
    state = JSONField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} |created by : {self.creator}'



