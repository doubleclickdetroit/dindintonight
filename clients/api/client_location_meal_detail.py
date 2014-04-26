from clients.models import ClientLocationMeal
from clients.serializers import ClientLocationMealSerializer, ClientLocationMealEditableSerializer
from core.api.RestView import RESTView


class ClientLocationMealDetail(RESTView):
    """
    Client Location Meal Detail API Class

    Example URL:
    /api/v1/clients/<client_id>/locations/<client_location_id>/meals/<pk>/
    """

    def get_object(self, pk, client_id, client_location_id):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the client location that you want to get detail on
        :client_id - Client Id that the location is related too
        :client_location_id - Client Location Id that the meal is linked too

        You must pass a PK in otherwise this will fail.

        If we cannot find the client location then we throw a 404
        """
        try:
            return ClientLocationMeal.objects.get(pk=pk, client_location__client__pk=client_id,
                                                  client_location__id=client_location_id)
        except ClientLocationMeal.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location Meal Detail

        :request - HTTP request from the api call
        :pk - PK of the client location that you want to get detail on
        :client_id - ID of the client that the location is related too

        You must pass in a PK otherwise this will fail.
        """
        client_location_meal = self.get_object(kwargs.get('pk'), kwargs.get('client_id'),
                                               kwargs.get('client_location_id'))

        client_location_meal_serialized = ClientLocationMealSerializer(client_location_meal)

        return client_location_meal_serialized.data

    def _handle_put(self, request, *args, **kwargs):
        """
        PUT handler for Client Location Meal Detail
        Sample Put Data:
        {
            "location": 1234
        }
        """
        post_data = request.DATA

        client_location_meal = self.get_object(kwargs.get('pk'), kwargs.get('client_id'),
                                               kwargs.get('client_location_id'))

        post_data['client_location'] = client_location_meal.client_location.pk
        post_data['meal'] = client_location_meal.pk

        serializer = ClientLocationMealEditableSerializer(client_location_meal, data=post_data)

        if serializer.is_valid():
            serializer.save()

            return ClientLocationMealSerializer(serializer.object).data

        return self.raise_bad_request(serializer.errors)
