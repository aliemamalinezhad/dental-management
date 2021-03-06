from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField
from ..managers import CustomUserManager
from users.models.access import Access


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True, blank=True)
    perm =JSONField(null=True, blank=True)
    role = models.CharField(max_length=300, null=True)
    access = models.ManyToManyField(Access,null=True,blank=True)
    city = models.CharField(max_length=300, null=True)
    id_code = models.BigIntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone',]

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'