# Local Apps
from clients.models import ClientLocation
from clients.serializers import ClientLocationSerializer
from core.api.RestView import RESTView


class ClientLocationList(RESTView):
    """
    Client Location List API Class


    Example URLs:

    /api/v1/clients/<client_id>/locations/
    """

    URL_NAME = 'api-v1-client-location-list'

    PER_PAGE = 20

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Client Location List

        :request - HTTP request from the api call
        :client_id - The ID of the client that we want to get locations for

        In the pages meta data it will have the full resource url for you to be able
        access the next and previous pages, this should symplify the front end devs
        lives and make it easy for them to build pagination into thre components.

        Also in the meta data you can access the current amount of data returned from
        the call as well as how many items exist overall.
        """
        self.URL_VARIABLES = {
            'client_id': kwargs.get('client_id')
        }

        results = ClientLocation.objects.prefetch_related('location').filter(client__pk=kwargs.get('client_id')).order_by(
            'location__state', 'location__city')

        return self.list_results(request, results, ClientLocationSerializer, use_cache=True,
                                      cache_time=self.CACHE_30_DAYS, cache_version=1)

    # def post(self, request, format=None):
    #     """
    #     POST handler for Package Level List

    #     :request - HTTP request from the api call

    #     Minimum Required Post Data (example json):
    #     {
    #         "name": "Some Name",
    #         "item": <item_id>
    #     }

    #     Upon successful post it will return back the newly created object in
    #     the response.

    #     If the requestor is not the item owner then they will get a 400 (bad
    #     request) or if they do not pass the minimum required data they also
    #     get a 400. Upon successful saving of the package they will get a 201
    #     (created) response with the newly created object.
    #     """
    #     # grab the post data
    #     post_data = request.DATA

    #     try:
    #         # try to get required items from the post data
    #         item        = Item.objects.get(pk=post_data.get('item'), author__pk=request.user.pk) # required
    #         name        = post_data.get('name') # required
    #         description = post_data.get('description', '') # not required
    #     except Exception, e:
    #         # if we cannot get the bare minimum of the items then we throw a 400 as
    #         # it is a bad request and cannot be processed
    #         return Response(e.message, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         # create the package from the item
    #         package = item.create_package(name, description)
    #     except Exception, e:
    #         # if we get any error of any sort then we throw a 500 for a server error
    #         return Response(e.message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #     # serialize the package
    #     package_serialized = PackageSerializer(package)

    #     # return back the data and a 201 response code since we created it
    #     return Response(package_serialized.data, status=status.HTTP_201_CREATED)
