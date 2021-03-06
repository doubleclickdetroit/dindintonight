from django.core.urlresolvers import reverse
from rest_framework import serializers

from locations.serializers import LocationSerializer
from users.serializers import UserSerializer
from vendors.models import VendorLocation, Vendor, VendorUser


class VendorLocationEditableSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = VendorLocation
        fields = ('id', 'vendor', 'location', 'address1', 'address2', 'address3', 'manager', 'created', 'modified',)
        read_only_fields = ('created', 'modified',)


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


class VendorUserSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    vendor = VendorSerializer()
    user = UserSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = VendorUser
        fields = ('id', 'vendor', 'user', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-vendor-user-detail', args=[obj.vendor.pk, obj.pk])