from django.core.urlresolvers import reverse
from rest_framework import serializers
from clients.models import ClientUser
from clients.serializers import ClientSerializer
from users.serializers import UserSerializer


class ClientUserSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client = ClientSerializer()
    user = UserSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientUser
        fields = ('id', 'client', 'user', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return ''  # reverse('api-v1-client-detail', args=[obj.pk])
