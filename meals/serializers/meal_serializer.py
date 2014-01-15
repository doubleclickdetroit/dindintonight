# Django Rest Framework
from rest_framework import serializers

# 3rd party
from meals.models import Meal

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'description', 'image', 'price', 'created', 'modified')
