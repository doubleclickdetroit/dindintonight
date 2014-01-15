# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from drops.models import DropMeal
from drops.serializers import DropMealSerializer

class DropMealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DropMeal.objects.all()
    serializer_class = DropMealSerializer
