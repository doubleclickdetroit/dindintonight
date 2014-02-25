# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from meals.models import Meal

class MealSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    city = serializers.CharField(max_length=255, min_length=1)
    description = serializers.CharField(max_length=45, min_length=1)
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Meal
        fields = ('id', 'vendor_location', 'description', 'price',
            'available_starting', 'available_ending', 'is_deleted',
            'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-meal-detail', args=[obj.vendor_location.vendor.pk,
            obj.vendor_location.pk, obj.pk])
