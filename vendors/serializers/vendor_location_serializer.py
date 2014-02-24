# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from vendors.models import VendorLocation

class VendorLocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    vendor_uri = serializers.SerializerMethodField('get_vendor_uri')
    location_uri = serializers.SerializerMethodField('get_location_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = VendorLocation
        fields = ('id', 'vendor', 'vendor_uri', 'location', 'location_uri',
            'address1', 'address2', 'address3', 'manager', 'created', 'modified',
            'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-vendor-location-detail', args=[obj.vendor.pk, obj.pk])

    def get_vendor_uri(self, obj):
        return reverse('api-v1-vendor-detail', args=[obj.vendor.pk])

    def get_location_uri(self, obj):
        return reverse('api-v1-location-detail', args=[obj.location.pk])
