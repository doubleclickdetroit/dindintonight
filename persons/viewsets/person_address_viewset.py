# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from persons.models import PersonAddress
from persons.serializers import PersonAddressSerializer

class PersonAddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PersonAddress.objects.all()
    serializer_class = PersonAddressSerializer
