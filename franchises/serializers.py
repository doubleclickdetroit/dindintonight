from django.core.urlresolvers import reverse
from rest_framework import serializers
from franchises.models import Franchise
from users.serializers import UserSerializer


class FranchiseSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    owner = UserSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Franchise
        fields = ('id', 'owner', 'name', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return ''  # reverse('api-v1-meal-detail', args=[obj.vendor_location.vendor.pk, obj.vendor_location.pk, obj.pk])
