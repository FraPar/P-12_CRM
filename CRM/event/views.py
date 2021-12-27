from rest_framework.viewsets import ModelViewSet
 
from .models import Event
from .serializers import EventSerializer
 
class EventViewset(ModelViewSet):
 
    serializer_class = EventSerializer
 
    def get_queryset(self):
        return Event.objects.all()
