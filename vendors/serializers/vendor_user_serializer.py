# Django
from django.core.urlresolvers import reverse

# Django Rest Framework
from rest_framework import serializers

# Local Apps
from users.serializers import UserSerializer
from vendors.models import VendorUser
from vendors.serializers import VendorSerializer


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
