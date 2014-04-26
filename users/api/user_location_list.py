from locations.models import Location
from users.models import UserLocation, User
from core.api import RESTView
from users.serializers import UserLocationEditableSerializer, UserLocationSerializerNoUserFK


class UserLocationList(RESTView):
    """
    Client List API Class

    Example URLs:

    /api/v1/clients/<client_id>/locations/
    """

    URL_NAME = 'api-v1-user-location-list'

    def _handle_get(self, request, *args, **kwargs):
        self.URL_VARIABLES = {
            'user_id': kwargs.get('user_id')
        }

        results = UserLocation.objects.filter(user__pk=kwargs.get('user_id')).prefetch_related('location')

        return self.list_results(request, results, UserLocationSerializerNoUserFK, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        Sample post data
        {
            "user": 1,
            "location": 1234
        }
        """
        post_data = request.DATA
        response = {}

        errors = False

        if post_data.get('location', None) is None:
            response['location'] = [
                'Location is a required field!',
            ]
            errors = True
        else:
            if Location.objects.filter(pk=post_data.get('location')).count() == 0:
                response['location'] = [
                    'Invalid location requested!',
                ]
                errors = True

        if User.objects.filter(pk=kwargs.get('user_id')).count() == 0:
            response['user'] = [
                'Invalid user requested!',
            ]
            errors = True
        else:
            post_data['user'] = kwargs.get('user_id')

        if errors:
            self.raise_bad_request(response)

        serializer = UserLocationEditableSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()

            return UserLocationSerializerNoUserFK(serializer.object).data

        return self.raise_bad_request(serializer.errors)

