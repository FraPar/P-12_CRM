# from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin

from . import models

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
    )
