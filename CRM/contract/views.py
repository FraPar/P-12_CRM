from rest_framework.viewsets import ModelViewSet
 
from .models import Contract
from .serializers import ContractSerializer
 
class ContractViewset(ModelViewSet):
 
    serializer_class = ContractSerializer
 
    def get_queryset(self):
        return Contract.objects.all()
