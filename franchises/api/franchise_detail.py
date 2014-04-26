from core.api import RESTView
from franchises.models import Franchise
from franchises.serializers import FranchiseSerializer


class FranchiseDetail(RESTView):
    """
    Franchise Detail API Class

    Example URLs:

    /api/v1/franchise/<pk>/
    """
    def get_object(self, pk):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the location that you want to get detail on
        :vendor_id - Vendor ID that you want to get a meal for
        :vendor_location_id - Vendor Location ID that you want to get a meal for

        If we cannot find the meal then we throw a 404
        """
        try:
            return Franchise.objects.get(pk=pk)
        except Franchise.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Franchise Detail

        :request - HTTP request from the api call
        :pk - PK of the franchise that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        franchise = self.get_object(kwargs.get('pk'))

        franchise_serialized = FranchiseSerializer(franchise)

        return franchise_serialized.data
