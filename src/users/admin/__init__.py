from django.contrib import admin

from users.admin.user import CustomUserAdmin
from users.models import (
    CustomUser as UserModel,
)

admin.site.register(UserModel, CustomUserAdmin)
