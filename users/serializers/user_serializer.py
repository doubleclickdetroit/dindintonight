# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# 3rd party
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'created', 'modified', 'resource_uri')

    def get_resource_uri(self, obj):
        return reverse('api-v1-user-detail', args=[obj.pk])
