from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from authentication.permissions import IsSupervisor, IsSales, IsSupport, IsClientSales, IsSupportOnEvent
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

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [IsSupervisor|IsSupport|IsSales]
        elif self.action in ['create'] :
            permission_classes = [IsSupervisor|IsSales]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsSupervisor|IsClientSales|IsSupportOnEvent]
        elif self.action in ['destroy']:
            permission_classes = [IsSupervisor|IsClientSales]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['support_contact', 'client__id']
    search_fields  = ['id', 'attendees', 'event_date', 'notes']

    def get_queryset(self):
        return Event.objects.all()