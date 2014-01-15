# Django Rest Framework
from rest_framework import serializers

# 3rd party
from drops.models import Drop

class DropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drop
        fields = ('id', 'location', 'date_and_time', 'timezone', 'created', 'modified')
