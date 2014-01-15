# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from drops.models import Drop
from drops.serializers import DropSerializer

class DropViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Drop.objects.all()
    serializer_class = DropSerializer
