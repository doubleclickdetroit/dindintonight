from core.api import RESTView
from meals.models import Meal
from meals.serializers import MealSerializer
from vendors.models import VendorLocation
import datetime


class MealList(RESTView):
    """
    Meal List API Class


    Example URLs:

    /api/v1/vendors/<vendor_id>/locations/<vendor_location_id>/meals/
    /api/v1/vendors/<vendor_id>/locations/<vendor_location_id>/meals/?show_deleted=true
    """

    URL_NAME = 'api-v1-meal-list'

    PER_PAGE = 20

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Meal List

        :request - HTTP request from the api call
        :vendor_id - Vendor ID that you want to get meals for
        :vendor_location_id - Vendor Location ID that you want to get meals for
        """
        self.URL_VARIABLES = {
            'vendor_location_id': kwargs.get('vendor_location_id'),
            'vendor_id': kwargs.get('vendor_id')
        }

        results = Meal.objects.prefetch_related('vendor_location__vendor').filter(
            vendor_location__pk=kwargs.get('vendor_location_id'),
            vendor_location__vendor__pk=kwargs.get('vendor_id')).order_by('available_starting')

        show_deleted = request.QUERY_PARAMS.get('show_deleted', False)

        if show_deleted in ['false', 0, False]:
            results = results.filter(is_deleted=False)

        return self.list_results(request, results, MealSerializer, use_cache=True, cache_time=self.CACHE_30_DAYS,
                                 cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        try:
            vendor_location = VendorLocation.objects.get(pk=kwargs.get('vendor_location_id'),
                                                         vendor__pk=kwargs.get('vendor_id'))
        except VendorLocation.DoesNotExist:
            self.raise_not_found()

        post_data = request.DATA
        post_data['vendor_location'] = vendor_location.pk
        serializer = MealSerializer(data=post_data)

        if post_data.get('available_starting', None) is not None:
            post_data['available_starting'] = datetime.datetime.strptime(post_data['available_starting'],
                                                                         '%m-%d-%Y').isoformat()

        if post_data.get('available_ending', None) is not None:
            post_data['available_ending'] = datetime.datetime.strptime(post_data['available_ending'],
                                                                       '%m-%d-%Y').isoformat()

        if serializer.is_valid():
            serializer.save()

            return serializer.data

        return self.raise_bad_request(serializer.errors)
