# Django Rest Framework
from rest_framework import serializers

# 3rd party
from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created')
