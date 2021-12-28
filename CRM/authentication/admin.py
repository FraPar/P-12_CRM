# from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class UsersAdmin(UserAdmin):
    list_display = (
        "username",
        "last_name",
        "first_name",
        "email",
        "is_active",
        "is_superuser",
    )
    list_display_links = (
        "username",
        "last_name",
        "first_name",
    )
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ("last_name", "first_name", "email")

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )