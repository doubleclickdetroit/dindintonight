# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from vendors.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    name = serializers.CharField(max_length=255, min_length=1)
    vendor_locations_uri = serializers.SerializerMethodField('get_vendor_locations_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'vendor_locations_uri', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-vendor-detail', args=[obj.pk])

    def get_vendor_locations_uri(self, obj):
        return reverse('api-v1-vendor-location-list', args=[obj.pk])
