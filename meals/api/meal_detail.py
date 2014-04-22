from core.api.RestView import RESTView
from meals.models import Meal
from meals.serializers import MealSerializer


class MealDetail(RESTView):
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
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Meal Detail

        :request - HTTP request from the api call
        :pk - PK of the location that you want to get detail on
        :vendor_id - Vendor ID that you want to get a meal for
        :vendor_location_id - Vendor Location ID that you want to get a meal for

        You must pass in a PK otherwise this will fail.
        """
        meal = self.get_object(kwargs.get('pk'), kwargs.get('vendor_id'), kwargs.get('vendor_location_id'))

        meal_serialized = MealSerializer(meal)

        return meal_serialized.data

    def _handle_put(self, request, *args, **kwargs):
        meal = self.get_object(kwargs.get('pk'), kwargs.get('vendor_id'), kwargs.get('vendor_location_id'))

        post_data = request.DATA
        post_data['vendor_location'] = meal.vendor_location.pk

        if post_data.get('price', None) is None:
            post_data['price'] = meal.price

        serializer = MealSerializer(meal, data=post_data)

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
