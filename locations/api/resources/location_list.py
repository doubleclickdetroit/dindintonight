# Local Apps
from core.api.RestView import RESTView
from locations.models import Location
from locations.serializers import LocationSerializer

class LocationList(RESTView):
    """
    Package List API Class


    Example URLs:

    /api/v1/locations/

    /api/v1/locations/?city=detroit

    /api/v1/locations/?state=mi

    /api/v1/locations/?city=detroit&state=mi

    /api/v1/locations/?zip_code=48092
    """

    URL_NAME = 'api-v1-location-list'

    PER_PAGE = 20

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Package List

        :request - HTTP request from the api call

        This will automatically pull out the requestors user id and only return
        back the requestors packages.

        In the pages meta data it will have the full resource url for you to be able
        access the next and previous pages, this should symplify the front end devs
        lives and make it easy for them to build pagination into thre components.

        Also in the meta data you can access the current amount of data returned from
        the call as well as how many items exist overall.
        """
        results = Location.objects.all().order_by('state', 'city')

        state = request.GET.get('state', None)
        city = request.GET.get('city', None)
        zip_code = request.GET.get('zip_code', None)

        if state is not None:
            results = results.filter(state__iexact=state)

        if city is not None:
            results = results.filter(city__iexact=city)

        if zip_code is not None:
            results = results.filter(zip_code=zip_code)

        return self.paginated_results(request, results, LocationSerializer, use_cache=True,
                                      cache_time=self.CACHE_30_DAYS, cache_version=1)
