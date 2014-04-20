from clients.models import Client
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

        return self.list_results(request, results, ClientSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
