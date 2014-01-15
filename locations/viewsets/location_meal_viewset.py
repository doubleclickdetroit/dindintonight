# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from locations.models import LocationMeal
from locations.serializers import LocationMealSerializer

class LocationMealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocationMeal.objects.all()
    serializer_class = LocationMealSerializer
