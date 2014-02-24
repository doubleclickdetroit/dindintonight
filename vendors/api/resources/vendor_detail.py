# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from vendors.models import Vendor
from vendors.serializers import VendorSerializer

class VendorDetail(APIView):
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
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET handler for Vendor Detail

        :request - HTTP request from the api call
        :pk - PK of the vendor that you want to get detail on

        You must pass in a PK otherwise this will fail.
        """
        vendor = self.get_object(pk)

        vendor_serialized = VendorSerializer(vendor)

        return Response(vendor_serialized.data)
