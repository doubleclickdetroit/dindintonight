from clients.models import Client
from clients.serializers import ClientSerializer
from core.api import RESTView


class ClientDetail(RESTView):
    """
    Client Detail API Class

    Example URL:
    /api/v1/clients/<pk>/
    """

    def get_object(self, pk):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the location that you want to get detail on

        You must pass a PK in otherwise this will fail.

        If we cannot find the client then we throw a 404
        """
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Detail

        :request - HTTP request from the api call
        :pk - PK of the client that you want to get detail on
        """
        client = self.get_object(kwargs.get('pk'))

        client_serialized = ClientSerializer(client)

        return client_serialized.data

    def _handle_put(self, request, *args, **kwargs):
        """
        PUT/PATCH handler for Client Detail

        Sample Post Data:
        {
            "name": "Detroit City Apartments"
        }
        """
        client = self.get_object(kwargs.get('pk'))

        serializer = ClientSerializer(client, data=request.DATA)

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
