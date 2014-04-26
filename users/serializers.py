from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.core.urlresolvers import reverse
from rest_framework import serializers
from locations.serializers import LocationSerializer
from users.models import User, UserLocation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    locations = LocationSerializer(source='locations', many=True)
    social_accounts = serializers.SerializerMethodField('get_social_accounts')
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'created', 'modified',
                  'social_accounts', 'locations', 'resource_uri',)
        read_only_fields = ('date_joined', 'created', 'modified',)

    def get_resource_uri(self, obj):
        return reverse('api-v1-user-detail', args=[obj.pk])

    def get_social_accounts(self, obj):
        try:
            return SocialAccountSerializer(SocialAccount.objects.filter(user=obj), many=True).data
        except SocialAccount.DoesNotExist:
            return None


class UserLocationSerializerNoUserFK(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    location = LocationSerializer()
    resource_uri = serializers.SerializerMethodField('get_resource_uri')

    class Meta:
        model = UserLocation
        fields = ('id', 'location', 'created', 'modified',)
        read_only_fields = ('created', 'modified',)

    def get_resource_uri(self, obj):
        return '' # reverse('api-v1-user-detail', args=[obj.pk])


class UserLocationEditableSerializerNoUserFK(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()

    class Meta:
        model = UserLocation
        fields = ('id', 'user', 'location', 'created', 'modified',)
        read_only_fields = ('created', 'modified',)


class SocialAccountSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    social_tokens = serializers.SerializerMethodField('get_social_tokens')

    class Meta:
        model = SocialAccount
        fields = ('id', 'provider', 'uid', 'last_login', 'date_joined', 'extra_data', 'social_tokens',)
        read_only_fields = ('provider', 'uid', 'last_login', 'date_joined', 'extra_data',)

    def get_social_tokens(self, obj):
        try:
            return SocialTokenSerializer(SocialToken.objects.filter(account=obj), many=True).data
        except SocialToken.DoesNotExist:
            return None


class SocialAppSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()

    class Meta:
        model = SocialApp
        fields = ('id', 'provider', 'name', 'client_id', 'key',)
        read_only_fields = ('provider', 'name', 'client_id', 'key',)


class SocialTokenSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.Field()
    app = SocialAppSerializer()

    class Meta:
        model = SocialToken
        fields = ('id', 'token', 'token_secret', 'expires_at',)
        read_only_fields = ('token', 'token_secret', 'expires_at',)
