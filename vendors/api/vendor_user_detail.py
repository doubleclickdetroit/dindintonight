from core.api import RESTView
from vendors.models import VendorUser
from vendors.serializers import VendorUserSerializer

class VendorUserDetail(RESTView):
    """
    Vendor User Detail API Class

    Example URL:
    /api/v1/vendors/<vendor_id>/users/<pk>/
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
            return VendorUser.objects.get(pk=pk, vendor__pk=vendor_id)
        except VendorUser.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Vendor User Detail

        :request - HTTP request from the api call

        Kwargs
        :pk - PK of the vendor user that you want to get detail on
        :vendor_id - Vendor Id that the user is related too

        You must pass in a PK otherwise this will fail.
        """
        vendor_user = self.get_object(kwargs.get('pk'), kwargs.get('vendor_id'))

        return self.detail_results(vendor_user, VendorUserSerializer)
