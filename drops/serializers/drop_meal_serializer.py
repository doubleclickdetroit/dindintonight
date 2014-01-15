# Django Rest Framework
from rest_framework import serializers

# 3rd party
from drops.models import DropMeal

class DropMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DropMeal
        fields = ('id', 'drop', 'meal', 'quantity', 'created', 'modified')
