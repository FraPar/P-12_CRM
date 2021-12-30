from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from authentication.permissions import IsSupervisor, IsSales, IsSupport
from .models import Event
from .serializers import EventSerializer
 
class EventViewset(
        CreateModelMixin, 
        RetrieveModelMixin, 
        UpdateModelMixin,
        DestroyModelMixin,
        ListModelMixin,
        viewsets.GenericViewSet
    ):

    permission_classes = [IsSupervisor|IsSupport|IsSales]
    serializer_class = EventSerializer
 
    def get_queryset(self):
        return Event.objects.all()

    def destroy(self, request, *args, **kwargs):
        event_id = request.path.split('/')[-2]
        eventset = Event.objects.filter(id=event_id)
        if eventset.exists():
                return super().destroy(request, *args, **kwargs)
        return Response({"Status":"Pas de problème trouvé"},status=status.HTTP_400_BAD_REQUEST)
