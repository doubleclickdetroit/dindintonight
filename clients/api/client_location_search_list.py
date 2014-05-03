from clients.models import ClientLocation
from clients.serializers import ClientLocationSerializer
from core.api import RESTView
from franchises.models import Franchise
from locations.models import Location


class ClientLocationSearchList(RESTView):
    """
    Search Client Location List API Class

    Example URLs:

    /api/v1/search/clients/locations/?city=detroit&state=mi
    /api/v1/search/clients/locations/?zip_code=48092
    /api/v1/search/clients/locations/?franchise=1
    """

    URL_NAME = 'api-v1-client-location-search-list'

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location List

        :request - HTTP request from the api call
        :client_id - The ID of the client that we want to get locations for
        """
        results = ClientLocation.objects.prefetch_related('location').prefetch_related('client').filter(
            meals__gt=0).order_by('location__state', 'location__city')

        state = request.GET.get('state', None)
        city = request.GET.get('city', None)
        zip_code = request.GET.get('zip_code', None)
        franchise = request.GET.get('franchise', None)

        response = {}

        if state is not None and city is not None:
            results = results.filter(location__state__iexact=state, location__city__iexact=city)
        elif zip_code is not None:
            try:
                location = Location.objects.get(zip_code=zip_code)
            except Location.DoesNotExist:
                response['zip_code'] = [
                    'Zip Code requested doesn\'t exist',
                ]
                return self.raise_bad_request(response)

            results = results.filter(location__state__iexact=location.state, location__city__iexact=location.city)
        elif franchise is not None:
            try:
                franchise = Franchise.objects.get(pk=franchise)
            except Location.DoesNotExist:
                response['franchise'] = [
                    'Franchise requested doesn\'t exist',
                ]
                return self.raise_bad_request(response)

            results = results.filter(client__franchise=franchise)

        else:
            if state is None:
                response['state'] = [
                    'State must be passed',
                ]

            if city is None:
                response['city'] = [
                    'City must be passed',
                ]

            if zip_code is None:
                response['zip_code'] = [
                    'Zip Code must be passed',
                ]

            if franchise is None:
                response['franchise'] = [
                    'Franchise must be passed',
                ]

            return self.raise_bad_request(response)

        return self.list_results(request, results, ClientLocationSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)