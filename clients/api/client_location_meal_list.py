from clients.models import ClientLocationMeal, Client, ClientLocation
from clients.serializers import ClientLocationMealSerializer, ClientLocationMealEditableSerializer
from core.api import RESTView
from meals.models import Meal


class ClientLocationMealList(RESTView):
    """
    Client Location Meal List API Class

    Example URLs:

    /api/v1/clients/<client_id>/locations/<client_location_id>/meals/
    """

    URL_NAME = 'api-v1-client-location-meal-list'

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location Meal List

        :request - HTTP request from the api call
        :client_id - The ID of the client that we want to get locations for
        """
        self.URL_VARIABLES = {
            'client_id': kwargs.get('client_id'),
            'client_location_id': kwargs.get('client_location_id')
        }

        results = ClientLocationMeal.objects.prefetch_related('meal').prefetch_related('client_location').\
            filter(client_location__pk=kwargs.get('client_location_id'),
                   client_location__client__pk=kwargs.get('client_id'))

        return self.list_results(request, results, ClientLocationMealSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        POST handler for Client Location Meal List
        Sample Post Data:
        {
            "location": 1234
        }
        """
        try:
            client = Client.objects.get(pk=kwargs.get('client_id'))
        except Client.DoesNotExist:
            self.raise_not_found()

        try:
            client_location = ClientLocation.objects.get(pk=kwargs.get('client_location_id'), client=client)
        except Client.DoesNotExist:
            self.raise_not_found()

        post_data = request.DATA

        try:
            meal = Meal.objects.get(pk=post_data.get('meal'))
        except Client.DoesNotExist:
            self.raise_not_found()

        post_data['client_location'] = client_location.pk

        serializer = ClientLocationMealEditableSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()

            return ClientLocationMealSerializer(serializer.object).data

        return self.raise_bad_request(serializer.errors)
