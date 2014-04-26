from core.api import RESTView
from vendors.models import VendorLocation
from vendors.serializers import VendorLocationSerializer, VendorLocationEditableSerializer


class VendorLocationList(RESTView):
    """
    Vendor Location List API Class

    Example URLs:

    /api/v1/vendors/<vendor_id>/locations/
    """

    URL_NAME = 'api-v1-vendor-location-list'

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Vendor Location List

        :request - HTTP request from the api call

        Kwargs:
        :vendor_id - The ID of the vendor that we want to get locations for
        """
        self.URL_VARIABLES = {
            'vendor_id': kwargs.get('vendor_id')
        }

        results = VendorLocation.objects.filter(vendor__pk=kwargs.get('vendor_id')).order_by(
            'location__state', 'location__city')

        return self.list_results(request, results, VendorLocationSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        Sample post data
{
    "vendor": 1,
    "location": 1234,
    "address1": "123 Test Lane",
    "address2": "Something Something Address 2",
    "address3": "Something Something Else Address 3",
    "manager": "This guy!"
}
        """
        serializer = VendorLocationEditableSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()

            vendor_serialized = VendorLocationSerializer(VendorLocation.objects.get(pk=serializer.data.get('id')))

            return vendor_serialized.data

        return self.raise_bad_request(serializer.errors)
