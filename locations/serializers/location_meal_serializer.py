# Django Rest Framework
from rest_framework import serializers

# 3rd party
from locations.models import LocationMeal

class LocationMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocationMeal
        fields = ('id', 'location', 'meal', 'created', 'modified')
