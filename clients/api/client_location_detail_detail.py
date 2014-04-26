from clients.models import ClientLocationDetail, ClientLocation
from clients.serializers import ClientLocationDetailSerializer
from core.api import RESTView


class ClientLocationDetailDetail(RESTView):
    """
    Client Location Detail Detail API Class

    Example URL:
    /api/v1/clients/<client_id>/locations/<client_location_id>/details/
    """

    def get_object(self, client_id, client_location_id, get_or_create=False):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the client location detail that you want to get detail on
        :client_id - Client Id that the detail is related too
        :client_location_id - Client Location ID that the detail is related too

        You must pass a PK in otherwise this will fail.

        If we cannot find the client location detail then we throw a 404
        """
        try:
            return ClientLocationDetail.objects.get(client_location__client__pk=client_id,
                                                    client_location__pk=client_location_id)
        except ClientLocationDetail.DoesNotExist:
            if get_or_create:
                return ClientLocationDetail.objects.create(client_location__pk=client_location_id)
            else:
                self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location Detail Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :client_id - ID of the client that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        client_location_detail = self.get_object(kwargs.get('client_id'), kwargs.get('client_location_id'))

        client_location_detail_serialized = ClientLocationDetailSerializer(client_location_detail)

        return client_location_detail_serialized.data

    def _handle_put(self, request, *args, **kwargs):
        """
        Sample Put Data:
        {
            "address1": "Address 1",
            "address2": "Address 2",
            "address3": "Address 2",
            "phone_number": "1 586 123 1234",
            "manager_name": "Some Manager"
        }
        """
        try:
            client_location = ClientLocation.objects.get(pk=kwargs.get('client_location_id'),
                                                         client__pk=kwargs.get('client_id'))
        except ClientLocation.DoesNotExist:
            self.raise_not_found()

        client_location_detail = self.get_object(kwargs.get('client_id'), kwargs.get('client_location_id'),
                                                 get_or_create=True)

        put_data = request.DATA
        put_data['client_location'] = client_location.pk

        serializer = ClientLocationDetailSerializer(client_location_detail, data=put_data)

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
