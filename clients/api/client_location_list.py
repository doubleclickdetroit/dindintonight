from clients.models import ClientLocation, Client
from clients.serializers import ClientLocationMinimumSerializer, ClientLocationEditableSerializer
from core.api.RestView import RESTView
from locations.models import Location


class ClientLocationList(RESTView):
    """
    Client Location List API Class

    Example URLs:

    /api/v1/clients/<client_id>/locations/
    """

    URL_NAME = 'api-v1-client-location-list'

    PER_PAGE = 20

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location List

        :request - HTTP request from the api call
        :client_id - The ID of the client that we want to get locations for
        """
        self.URL_VARIABLES = {
            'client_id': kwargs.get('client_id')
        }

        results = ClientLocation.objects.prefetch_related('location').filter(client__pk=kwargs.get('client_id')).\
            order_by('location__state', 'location__city')

        return self.list_results(request, results, ClientLocationMinimumSerializer, use_cache=True,
                                      cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        POST handler for Client Location List
        Sample Post Data:
        {
            "location": 1234
        }
        """
        try:
            client = Client.objects.get(pk=kwargs.get('client_id'))
        except Client.DoesNotExist:
            self.raise_not_found()

        post_data = request.DATA
        post_data['client'] = client.pk

        try:
            Location.objects.get(pk=post_data.get('location', None))
        except Location.DoesNotExist:
            response = {
                'location': [
                    'Invalid location!',
                ]
            }
            self.raise_bad_request(response)

        serializer = ClientLocationEditableSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()

            return ClientLocationMinimumSerializer(ClientLocation.objects.get(pk=serializer.data.get('id'))).data

        return self.raise_bad_request(serializer.errors)
