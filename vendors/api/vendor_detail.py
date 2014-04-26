from core.api import RESTView
from vendors.models import Vendor
from vendors.serializers import VendorSerializer

class VendorDetail(RESTView):
    """
    Vendor Detail API Class

    Example URL:
    /api/v1/vendors/<pk>/
    """

    def get_object(self, pk):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the vendor that you want to get detail on

        You must pass a PK in otherwise this will fail.

        If we cannot find the vendor then we throw a 404
        """
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Vendor Detail

        :request - HTTP request from the api call
        :pk - PK of the vendor that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        vendor = self.get_object(kwargs.get('pk'))

        return self.detail_results(vendor, VendorSerializer)
