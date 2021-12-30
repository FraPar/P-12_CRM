from django.db import models
from authentication.models import User
from client.models import Client

class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name="Contract's status")
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=True)
