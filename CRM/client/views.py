from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets

from authentication.permissions import IsSupervisor
from .serializers import ClientSerializer
from .models import Client
from .serializers import ClientSerializer
 
class ClientViewset(
        CreateModelMixin, 
        RetrieveModelMixin, 
        UpdateModelMixin,
        DestroyModelMixin,
        ListModelMixin,
        viewsets.GenericViewSet
    ):

    permission_classes = [IsAuthenticated, IsSupervisor]
    serializer_class = ClientSerializer
 
    def get_queryset(self):
        return Client.objects.all()
