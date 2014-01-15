# Django Rest Framework
from rest_framework import serializers

# 3rd party
from locations.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'city', 'state', 'zip', 'created', 'modified')
