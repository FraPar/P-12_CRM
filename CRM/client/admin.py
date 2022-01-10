# from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin

from . import models

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'mobile',
        'company_name',
        'sales_contact',
    )
    list_filter = ["id", "last_name", "sales_contact"]
    search_fields = ("first_name", "last_name", "email", "phone", "mobile", "company_name")
