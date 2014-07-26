from django.core.urlresolvers import reverse
from rest_framework import serializers

from meals.models import Meal, MealImage


class MealImageSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = MealImage
        fields = ('id', 'meal', 'name', 'description', 'location', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return ''
        # return reverse('api-v1-meal-detail', args=[obj.vendor_location.vendor.pk, obj.vendor_location.pk, obj.pk])

class MealSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    city = serializers.CharField(max_length=255, min_length=1)
    description = serializers.CharField(max_length=45, min_length=1)
    images = MealImageSerializer(source='images', required=False)
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Meal
        fields = ('id', 'vendor_location', 'description', 'price', 'available_starting', 'available_ending',
                  'is_deleted', 'created', 'images', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-meal-detail', args=[obj.vendor_location.vendor.pk,
                                                   obj.vendor_location.pk, obj.pk])
