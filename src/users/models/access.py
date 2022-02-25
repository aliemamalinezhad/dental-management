from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField
from utils import GeneralModel


class Access(GeneralModel):
    actions = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.actions