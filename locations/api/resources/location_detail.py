# Local Apps
from core.api.RestView import RESTView
from locations.models import Location
from locations.serializers import LocationSerializer

class LocationDetail(RESTView):
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
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Location Detail

        :request - HTTP request from the api call
        :pk - PK of the location that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        location = self.get_object(kwargs.get('pk'))

        location_serialized = LocationSerializer(location)

        return location_serialized.data