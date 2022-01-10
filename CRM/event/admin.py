from django.contrib import admin
from . import models

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client_id',
        'support_contact',
        'event_status',
        'attendees',
        'event_date',
        'notes',
    )
    list_filter = ["id", "client_id", "support_contact", "event_status", ]
    search_fields = ("notes",)