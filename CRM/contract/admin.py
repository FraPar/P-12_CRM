from django.contrib import admin
from . import models

@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sales_contact',
        'client_id',
        'status',
        'amount',
        'payment_due',
    )
    list_filter = ["id", "sales_contact", "client_id", "status","payment_due"]
    search_fields = ("client_id", "status", "amount")