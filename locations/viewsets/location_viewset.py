# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from locations.models import Location
from locations.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
