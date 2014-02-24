# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from clients.models import ClientLocation

class ClientLocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client_uri = serializers.SerializerMethodField('get_client_uri')
    location_uri = serializers.SerializerMethodField('get_location_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocation
        fields = ('id', 'client', 'client_uri', 'location', 'location_uri', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client.pk, obj.pk])

    def get_client_uri(self, obj):
        return reverse('api-v1-client-detail', args=[obj.client.pk])

    def get_location_uri(self, obj):
        return reverse('api-v1-location-detail', args=[obj.location.pk])
