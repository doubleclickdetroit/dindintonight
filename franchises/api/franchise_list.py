from core.api import RESTView
from franchises.models import Franchise
from franchises.serializers import FranchiseSerializer


class FranchiseList(RESTView):
    """
    Franchise List API Class

    Example URLs:

    /api/v1/franchise/
    """

    URL_NAME = 'api-v1-franchise-list'

    PER_PAGE = 50

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Franchise List

        :request - HTTP request from the api call
        """
        results = Franchise.objects.all()

        return self.list_results(request, results, FranchiseSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)
