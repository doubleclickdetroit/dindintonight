from users.models import UserLocation
from core.api.RestView import RESTView
from users.serializers import UserLocationSerializerNoUserFK


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

        results = UserLocation.objects.filter(user__pk=kwargs.get('user_id'))

        return self.list_results(request, results, UserLocationSerializerNoUserFK, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

#     def _handle_post(self, request, *args, **kwargs):
#         """
#         Sample post data
# {
#     "first_name": "Robert",
#     "last_name": "Garrison Jr.",
#     "username": "rgarrisonjr",
#     "email": "rob+1@testingthisout.com",
#     "password": "testingthis"
# }
#         """
#         post_data = request.DATA
#         response = {}
#
#         errors = False
#
#         if post_data.get('first_name', None) is None:
#             response['first_name'] = [
#                 'First name is a required field!',
#             ]
#             errors = True
#
#         if post_data.get('last_name', None) is None:
#             response['last_name'] = [
#                 'Last name is a required field!',
#             ]
#             errors = True
#
#         if post_data.get('username', None) is None:
#             response['username'] = [
#                 'Username is a required field!',
#             ]
#             errors = True
#         else:
#             if User.objects.filter(username=post_data.get('username')).count() > 0:
#                 response['username'] = [
#                     'Username "{0}" is currently taken, please try another or request a password reset.'.format(
#                         post_data.get('username')),
#                 ]
#                 errors = True
#
#         if post_data.get('email', None) is None:
#             response['email'] = [
#                 'Email is a required field!',
#             ]
#             errors = True
#         else:
#             if User.objects.filter(email=post_data.get('email')).count() > 0:
#                 response['email'] = [
#                     'Email "{0}" is currently in use, please try another or request a password reset.'.format(
#                         post_data.get('email')),
#                 ]
#                 errors = True
#
#         if post_data.get('password', None) is None:
#             response['password'] = [
#                 'Password is a required field!',
#             ]
#             errors = True
#
#         if errors:
#             self.raise_bad_request(response)
#
#         user = User.objects.create_user(first_name=post_data.get('first_name'),
#                                         last_name=post_data.get('last_name'),
#                                         username=post_data.get('username'),
#                                         email=post_data.get('email'),
#                                         password=post_data.get('password'))
#
#         return self.detail_results(user, UserSerializer)
