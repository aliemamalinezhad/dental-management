from django.contrib import admin


class AccessAdmin(admin.ModelAdmin):
    list_display = ['actions',]
