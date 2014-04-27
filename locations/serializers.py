from django.core.urlresolvers import reverse
from rest_framework import serializers
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    city = serializers.CharField(max_length=255, min_length=1)
    state = serializers.CharField(max_length=255, min_length=1)
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Location
        fields = ('id', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-location-detail', args=[obj.pk])
