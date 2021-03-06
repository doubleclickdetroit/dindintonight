from clients.models import ClientLocation
from clients.serializers import ClientLocationSerializer, ClientLocationEditableSerializer
from core.api import RESTView
from locations.models import Location


class ClientLocationDetail(RESTView):
    """
    Client Location Detail API Class

    Example URL:
    /api/v1/clients/<client_id>/locations/<pk>/
    """

    def get_object(self, pk, client_id):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the client location that you want to get detail on
        :client_id - Client Id that the location is related too

        You must pass a PK in otherwise this will fail.

        If we cannot find the client location then we throw a 404
        """
        try:
            return ClientLocation.objects.get(pk=pk, client__pk=client_id)
        except ClientLocation.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :client_id - ID of the client that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        client_location = self.get_object(kwargs.get('pk'), kwargs.get('client_id'))

        client_location_serialized = ClientLocationSerializer(client_location)

        return client_location_serialized.data

    def _handle_put(self, request, *args, **kwargs):
        """
        PUT handler for Client Location Detail
        Sample Put Data:
        {
            "location": 1234
        }
        """
        client_location = self.get_object(kwargs.get('pk'), kwargs.get('client_id'))

        post_data = request.DATA
        post_data['client'] = client_location.client.pk

        try:
            Location.objects.get(pk=post_data.get('location', None))
        except Location.DoesNotExist:
            response = {
                'location': [
                    'Invalid location!',
                ]
            }
            self.raise_bad_request(response)

        serializer = ClientLocationEditableSerializer(client_location, data=post_data)

        if serializer.is_valid():
            serializer.save()

            return ClientLocationSerializer(serializer.object).data

        return self.raise_bad_request(serializer.errors)
