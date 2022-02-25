from django.contrib import admin

from users.admin.user import CustomUserAdmin
from users.admin.access import AccessAdmin
from users.models import (
    CustomUser as UserModel,
)
from users.models import (
    Access as AccessModel
)


admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(AccessModel, AccessAdmin)
