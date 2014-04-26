from core.api import RESTView
from users.models import User
from users.serializers import UserSerializer


class UserDetail(RESTView):
    """
    Vendor User Detail API Class

    Example URL:
    /api/v1/vendors/<vendor_id>/users/<pk>/
    """

    def get_object(self, pk):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the user that you want to get detail on

        You must pass a PK in otherwise this will fail.
        """
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for User Detail

        :request - HTTP request from the api call

        Kwargs
        :pk - PK of the user that you want to get detail on
        """
        user = self.get_object(kwargs.get('pk'))

        return self.detail_results(user, UserSerializer)

    def _handle_put(self, request, *args, **kwargs):
        """
        PUT handler for User Detail

        :request - HTTP request from the api call

        Here is how you change the user:
        {
            "username": "rob",                  OPTIONAL
            "first_name": "Roberto",            OPTIONAL
            "last_name": "Garrison III",        OPTIONAL
            "email": "rgarrison3@gmail.com"     OPTIONAL
        }

        if you want to change the password pass in the following json fields:
        {
            "username": "rob",                  OPTIONAL
            "first_name": "Roberto",            OPTIONAL
            "last_name": "Garrison III",        OPTIONAL
            "email": "rgarrison3@gmail.com",    OPTIONAL
            "password_1": "myPa55W0rd!",        REQUIRED
            "password_2": "myPa55W0rd!"         REQUIRED
        }

        Kwargs
        :pk - PK of the user that you want to get detail on
        """
        user = self.get_object(kwargs.get('pk'))
        response = {}

        put_data = request.DATA
        errors = False

        if put_data.get('username', None) is not None:
            if user.username != put_data.get('username') and User.objects.filter(username=put_data.get('username')).count() > 0:
                response['username'] = [
                    'Username "{0}" is currently taken, please try another.'.format(
                        put_data.get('username')),
                ]
                errors = True

        if put_data.get('email', None) is not None:
            if user.email != put_data.get('email') and User.objects.filter(email=put_data.get('email')).count() > 0:
                response['email'] = [
                    'Email "{0}" is currently in use, please try another.'.format(
                        put_data.get('email')),
                ]
                errors = True

        if put_data.get('password_1', None) is not None and put_data.get('password_2', None) is not None:
            if put_data.get('password_1') == put_data.get('password_2'):
                # update the password
                user.set_password(put_data.get('password_1'))
            else:
                response['password_1'] = [
                    'Password\'s don\'t match please try again!',
                ]
                response['password_2'] = [
                    'Password\'s don\'t match please try again!',
                ]
                errors = True

        if errors:
            self.raise_bad_request(response)

        serializer = UserSerializer(user, data=put_data)

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
