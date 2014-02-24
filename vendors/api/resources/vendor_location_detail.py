# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from vendors.models import VendorLocation
from vendors.serializers import VendorLocationSerializer

class VendorLocationDetail(APIView):
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
            raise Http404

    def get(self, request, vendor_id, pk, format=None):
        """
        GET handler for Vendor Location Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :vendor_id - Vendor Id that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        vendor_location = self.get_object(pk, vendor_id)

        vendor_location_serialized = VendorLocationSerializer(vendor_location)

        return Response(vendor_location_serialized.data)
