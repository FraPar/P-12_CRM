from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from authentication.permissions import IsSupervisor, IsSales, IsSupport, IsClientSales, IsSupportOnEvent
from .models import Contract
from .serializers import ContractSerializer
 
class ContractViewset(
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
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsSupervisor|IsClientSales]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    serializer_class = ContractSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['sales_contact', 'client']
    search_fields  = ['id', 'status', 'amount', 'payment_due']

    def get_queryset(self):
        return Contract.objects.all()
