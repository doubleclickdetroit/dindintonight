from rest_framework import serializers

from franchises.serializers import FranchiseSerializer
from leads.models import Lead


class LeadEditableSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = Lead
        fields = ('id', 'franchise', 'first_name', 'last_name', 'email', 'created', 'modified')
        read_only_fields = ('created', 'modified',)


class LeadSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    franchise = FranchiseSerializer()
    first_name = serializers.CharField(max_length=125, min_length=1)
    last_name = serializers.CharField(max_length=125, min_length=1)
    email = serializers.EmailField(max_length=255)
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Lead
        fields = ('id', 'franchise', 'first_name', 'last_name', 'email', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return ''
        # return reverse('api-v1-meal-detail', args=[obj.vendor_location.vendor.pk,
        #                                            obj.vendor_location.pk, obj.pk])
