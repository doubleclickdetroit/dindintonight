from clients.models import Client, ClientUser
from clients.serializers import ClientSerializer
from core.api.RestView import RESTView


class ClientList(RESTView):
    """
    Client List API Class

    Example URLs:

    /api/v1/clients/
    """

    URL_NAME = 'api-v1-client-list'

    def _handle_get(self, request, *args, **kwargs):
        results = Client.objects.all()

        user = request.GET.get('user', None)

        if user is not None:
            results = results.filter(users__pk=user)

        return self.list_results(request, results, ClientSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        Sample post data:
        {
            "name": "Test by Rob"
        }
        """
        serializer = ClientSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()

            # create the user to link them to the client they just created
            ClientUser.objects.create(client=serializer.object, user=request.user)

            return serializer.data

        return self.raise_bad_request(serializer.errors)
