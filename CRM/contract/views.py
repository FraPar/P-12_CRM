from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets

from authentication.permissions import IsSupervisor, IsSales, IsSupport
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

    permission_classes = [IsSupervisor|IsSupport|IsSales]
    serializer_class = ContractSerializer
 
    def get_queryset(self):
        return Contract.objects.all()
