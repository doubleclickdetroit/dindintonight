# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from clients.models import ClientLocationDetail
from clients.serializers import ClientLocationDetailSerializer

class ClientLocationDetailDetail(APIView):
    """
    Client Location Detail Detail API Class

    Example URL:
    /api/v1/clients/<client_id>/locations/<client_location_id>/details/
    """

    def get_object(self, client_id, client_location_id):
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
            raise Http404

    def get(self, request, client_id, client_location_id, format=None):
        """
        GET handler for Client Location Detail Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :client_id - ID of the client that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        client_location_detail = self.get_object(client_id, client_location_id)

        client_location_detail_serialized = ClientLocationDetailSerializer(client_location_detail)

        return Response(client_location_detail_serialized.data)
