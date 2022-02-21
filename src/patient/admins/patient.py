from django.contrib import admin

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name','city']
    list_filter = ['city']
