from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

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
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        print("self.action")
        print(self.action)
        if self.action in ['list','retrieve']:
            print("Reader")
            permission_classes = [IsSupervisor|IsSupport|IsSales]
        elif self.action in ['create'] :
            print("Creater")
            permission_classes = [IsSupervisor|IsSales]
        elif self.action in ['update', 'partial_update', 'destroy']:
            print("Owner")
            permission_classes = [IsSupervisor|IsClientSales]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    serializer_class = ContractSerializer
 
    def get_queryset(self):
        return Contract.objects.all()
