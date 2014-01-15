# Django Rest Framework
from rest_framework import serializers

# 3rd party
from persons.models import PersonAddress

class PersonAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonAddress
        fields = ('id', 'person', 'address', 'created', 'modified')
