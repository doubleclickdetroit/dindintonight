import re
from django.core import validators
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from clients.models import Client, ClientLocationDetail, ClientLocation, ClientUser, ClientLocationMeal
from locations.serializers import LocationSerializer
from meals.serializers import MealSerializer
from users.serializers import UserSerializer


class ClientCreationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, min_length=1,
                                     validators=[
                                         validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                   _('Enter a valid username.'), 'invalid')
                                     ])
    first_name = serializers.CharField(max_length=30, min_length=1)
    last_name = serializers.CharField(max_length=30, min_length=1)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, min_length=6)


class ClientLocationDetailSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client_location_uri = serializers.SerializerMethodField('get_client_location_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocationDetail
        fields = ('id', 'client_location', 'client_location_uri', 'address1', 'address2', 'address3', 'phone_number',
                  'manager_name', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail-detail', args=[obj.client_location.client.pk,
                                                                     obj.client_location.pk])

    def get_client_location_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client_location.client.pk, obj.client_location.pk])


class ClientLocationMinimumSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    location = LocationSerializer()
    details = ClientLocationDetailSerializer(source='details', required=False)
    client_uri = serializers.SerializerMethodField('get_client_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocation
        fields = ('id', 'client', 'client_uri', 'location', 'details', 'created', 'modified', 'resource_uri')
        read_only_fields = ('client', 'created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client.pk, obj.pk])

    def get_client_uri(self, obj):
        return reverse('api-v1-client-detail', args=[obj.client.pk])


class ClientLocationEditableSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = ClientLocation
        fields = ('id', 'client', 'location', 'created', 'modified')
        read_only_fields = ('created', 'modified',)


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    name = serializers.CharField(max_length=255, min_length=1)
    client_locations_uri = serializers.SerializerMethodField('get_client_locations_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = Client
        fields = ('id', 'name', 'client_locations_uri', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-detail', args=[obj.pk])

    def get_client_locations_uri(self, obj):
        return reverse('api-v1-client-location-list', args=[obj.pk])


class ClientLocationSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client = ClientSerializer()
    location = LocationSerializer()
    details = ClientLocationDetailSerializer(source='details', required=False)
    client_uri = serializers.SerializerMethodField('get_client_uri')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocation
        fields = ('id', 'client', 'client_uri', 'location', 'details', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-detail', args=[obj.client.pk, obj.pk])

    def get_client_uri(self, obj):
        return reverse('api-v1-client-detail', args=[obj.client.pk])


class ClientLocationMealSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client_location = ClientLocationSerializer()
    meal = MealSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientLocationMeal
        fields = ('id', 'client_location', 'meal', 'is_enabled', 'created', 'modified')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-client-location-meal-detail', args=[obj.client_location.client.pk,
                                                                   obj.client_location.pk, obj.pk])


class ClientLocationMealEditableSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model = ClientLocationMeal
        fields = ('id', 'client_location', 'meal', 'is_enabled', 'created', 'modified')
        read_only_fields = ('created', 'modified',)


class ClientUserSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    client = ClientSerializer()
    user = UserSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = ClientUser
        fields = ('id', 'client', 'user', 'created', 'modified', 'resource_uri')
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return ''  # reverse('api-v1-client-detail', args=[obj.pk])
