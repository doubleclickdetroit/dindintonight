from users.models import User
from clients.models import Client, ClientUser
from clients.serializers import ClientSerializer
from core.api.RestView import RESTView
from core.utils import debug_print


class ClientList(RESTView):
    """
    Client List API Class

    Example URLs:

    /api/v1/clients/
    """
    def _handle_post(self, request, *args, **kwargs):
        post_data = request.DATA
        debug_print('post data is as follows', color='blue')
        debug_print(post_data, color='blue')
        response = {}

        errors = False

        if post_data.get('first_name', None) is None:
            response['first_name'] = [
                'First name is a required field!',
            ]
            errors = True

        if post_data.get('last_name', None) is None:
            response['last_name'] = [
                'Last name is a required field!',
            ]
            errors = True

        if post_data.get('username', None) is None:
            response['username'] = [
                'Username is a required field!',
            ]
            errors = True

        if post_data.get('email', None) is None:
            response['email'] = [
                'Email is a required field!',
            ]
            errors = True

        if post_data.get('password', None) is None:
            response['password'] = [
                'Password is a required field!',
            ]
            errors = True

        if errors:
            self.raise_bad_request(response)

        user = User.objects.create_user(first_name=post_data.get('first_name'),
                                        last_name=post_data.get('last_name'),
                                        username=post_data.get('username'),
                                        email=post_data.get('email'),
                                        password=post_data.get('password'))
        client = Client.objects.create(name='{0} {1}'.format(post_data.get('first_name'), post_data.get('last_name')))
        ClientUser.objects.create(client=client, user=user)
        return self.detail_results(client, ClientSerializer)
