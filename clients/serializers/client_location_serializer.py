from django.core.urlresolvers import reverse
from rest_framework import serializers
from clients.models import ClientLocation
from locations.serializers import LocationSerializer


class ClientLocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client_uri = serializers.SerializerMethodField('get_client_uri')
    location = LocationSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocation
        fields = ('id', 'client', 'client_uri', 'location', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client.pk, obj.pk])

    def get_client_uri(self, obj):
        return reverse('api-v1-client-detail', args=[obj.client.pk])
