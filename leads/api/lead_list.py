from leads.models import Lead
from leads.serializers import LeadSerializer, LeadEditableSerializer
from franchises.models import Franchise
from core.api import RESTView


class LeadList(RESTView):
    """
    Lead List API Class

    Example URLs:

    /api/v1/franchise/<pk>/leads/
    """

    URL_NAME = 'api-v1-lead-list'

    def _handle_get(self, request, *args, **kwargs):
        try:
            franchise = Franchise.objects.get(pk=kwargs.get('franchise_id'))
        except Franchise.DoesNotExist:
            self.raise_not_found()

        results = Lead.objects.filter(franchise=franchise)

        return self.list_results(request, results, LeadSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        """
        POST handler for Client Location List
        Sample Post Data:
        {
            "location": 1234
        }
        """
        try:
            franchise = Franchise.objects.get(pk=kwargs.get('franchise_id'))
        except Franchise.DoesNotExist:
            self.raise_not_found()

        post_data = request.DATA
        post_data['franchise'] = franchise.pk

        serializer = LeadEditableSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()

            return LeadSerializer(serializer.object).data

        return self.raise_bad_request(serializer.errors)
