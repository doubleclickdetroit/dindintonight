# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from meals.models import Meal
from meals.serializers import MealSerializer

class MealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
