from django.core.urlresolvers import reverse
from rest_framework import serializers
from clients.models import ClientLocationDetail


class ClientLocationDetailSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client_location_uri = serializers.SerializerMethodField('get_client_location_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocationDetail
        fields = ('id', 'client_location', 'client_location_uri', 'address1', 'address2', 'address3', 'phone_number',
                  'manager_name', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail-detail', args=[obj.client_location.client.pk,
                                                                     obj.client_location.pk])

    def get_client_location_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client_location.client.pk, obj.client_location.pk])
