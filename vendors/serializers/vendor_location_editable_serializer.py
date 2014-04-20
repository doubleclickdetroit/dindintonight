from rest_framework import serializers
from vendors.models import VendorLocation


class VendorLocationEditableSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = VendorLocation
        fields = ('id', 'vendor', 'location', 'address1', 'address2', 'address3', 'manager', 'created', 'modified',)
        read_only_fields = ('created', 'modified',)
