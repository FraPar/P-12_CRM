from rest_framework.serializers import ModelSerializer
 
from .models import Event
 
class EventSerializer(ModelSerializer):
 
    class Meta:
        model = Event
        fields = ['client',
                  'date_created',
                  'date_updated',
                  'support_contact',
                  'event_status',
                  'attendees',
                  'event_date',
                  'notes']
