from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    SUPERVISOR = 'SUPERVISOR'
    SALES = 'SALES'
    SUPPORT = 'SUPPORT'

    ROLE_CHOICES = (
        (SUPERVISOR, 'Supervisor'),
        (SALES, 'Sales'),
        (SUPPORT, 'Support'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')