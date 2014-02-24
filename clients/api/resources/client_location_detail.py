# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from clients.models import ClientLocation
from clients.serializers import ClientLocationSerializer

class ClientLocationDetail(APIView):
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
            raise Http404

    def get(self, request, client_id, pk, format=None):
        """
        GET handler for Client Location Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :client_id - ID of the client that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        client_location = self.get_object(pk, client_id)

        client_location_serialized = ClientLocationSerializer(client_location)

        return Response(client_location_serialized.data)
