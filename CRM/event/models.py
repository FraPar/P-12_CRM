from django.db import models
from authentication.models import User
from client.models import Client
from contract.models import Contract


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=250)
