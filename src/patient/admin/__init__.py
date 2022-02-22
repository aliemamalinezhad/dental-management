from django.contrib import admin

from patient.admin.patient import PatientAdmin
from patient.models import (
    Patient as PatientModel,
)

admin.site.register(PatientModel, PatientAdmin)
