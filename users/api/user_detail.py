from core.api.RestView import RESTView
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
        :pk - PK of the vendor user that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        user = self.get_object(kwargs.get('pk'))

        return self.detail_results(user, UserSerializer)
