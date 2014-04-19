from core.api.RestView import RESTView
from vendors.models import VendorLocation
from vendors.serializers import VendorLocationSerializer

class VendorLocationDetail(RESTView):
    """
    Vendor Location Detail API Class

    Example URL:
    /api/v1/vendors/<vendor_id>/locations/<pk>/
    """

    def get_object(self, pk, vendor_id):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the vendor location that you want to get detail on
        :vendor_id - Vendor Id that the location is related too

        You must pass a PK in otherwise this will fail.

        If we cannot find the vendor location then we throw a 404
        """
        try:
            return VendorLocation.objects.get(pk=pk, vendor__pk=vendor_id)
        except VendorLocation.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Vendor Location Detail

        :request - HTTP request from the api call

        Kwargs
        :pk - PK of the client location that you want to get detail on
        :vendor_id - Vendor Id that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        vendor_location = self.get_object(kwargs.get('pk'), kwargs.get('vendor_id'))

        return self.detail_results(vendor_location, VendorLocationSerializer)
