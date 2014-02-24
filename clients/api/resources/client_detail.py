# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from clients.models import Client
from clients.serializers import ClientSerializer

class ClientDetail(APIView):
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
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET handler for Client Detail

        :request - HTTP request from the api call
        :pk - PK of the client that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        client = self.get_object(pk)

        client_serialized = ClientSerializer(client)

        return Response(client_serialized.data)
