# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from locations.models import Location
from locations.serializers import LocationSerializer

class LocationDetail(APIView):
    """
    Location Detail API Class

    Example URL:
    /api/v1/locations/<pk>/
    """

    def get_object(self, pk):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the location that you want to get detail on

        You must pass a PK in otherwise this will fail.

        If we cannot find the package then we throw a 404
        """
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET handler for Location Detail

        :request - HTTP request from the api call
        :pk - PK of the location that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        location = self.get_object(pk)

        location_serialized = LocationSerializer(location)

        return Response(location_serialized.data)