# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from vendors.models import VendorLocation
from locations.serializers import LocationSerializer

class VendorLocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    vendor_uri = serializers.SerializerMethodField('get_vendor_uri')
    location = LocationSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')
    meals_uri = serializers.SerializerMethodField('get_meals_uri')

    class Meta:
        model = VendorLocation
        fields = ('id', 'vendor', 'vendor_uri', 'location', 'address1',
            'address2', 'address3', 'manager', 'meals_uri', 'created',
            'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-vendor-location-detail', args=[obj.vendor.pk, obj.pk])

    def get_vendor_uri(self, obj):
        return reverse('api-v1-vendor-detail', args=[obj.vendor.pk])

    def get_meals_uri(self, obj):
        return reverse('api-v1-meal-list', args=[obj.vendor.pk, obj.pk])
