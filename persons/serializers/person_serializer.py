# Django Rest Framework
from rest_framework import serializers

# 3rd party
from persons.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'email', 'created')
