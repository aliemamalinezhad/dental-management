from django.contrib import admin

from patient.admins.patient import PatientAdmin
from patient.models import (
    Patient as PatientModel,
)

admin.site.register(PatientModel, PatientAdmin)
