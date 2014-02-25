# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from meals.models import Meal
from meals.serializers import MealSerializer

class MealDetail(APIView):
    """
    Meal Detail API Class


    Example URLs:

    /api/v1/vendors/<vendor_id>/locations/<vendor_location_id>/meals/<pk>/
    """

    def get_object(self, pk, vendor_id, vendor_location_id):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the location that you want to get detail on
        :vendor_id - Vendor ID that you want to get a meal for
        :vendor_location_id - Vendor Location ID that you want to get a meal for

        If we cannot find the meal then we throw a 404
        """
        try:
            return Meal.objects.get(pk=pk, vendor_location_id__pk=vendor_location_id,
                vendor_location_id__vendor__pk=vendor_id)
        except Meal.DoesNotExist:
            raise Http404

    def get(self, request, pk, vendor_id, vendor_location_id, format=None):
        """
        GET handler for Meal Detail

        :request - HTTP request from the api call
        :pk - PK of the location that you want to get detail on
        :vendor_id - Vendor ID that you want to get a meal for
        :vendor_location_id - Vendor Location ID that you want to get a meal for

        You must pass in a PK otherwise this will fail.
        """
        meal = self.get_object(pk, vendor_id, vendor_location_id)

        meal_serialized = MealSerializer(meal)

        return Response(meal_serialized.data)
