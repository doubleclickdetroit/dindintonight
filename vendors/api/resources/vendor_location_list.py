# Django
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Local Apps
from vendors.models import VendorLocation
from vendors.serializers import VendorLocationSerializer

class VendorLocationList(APIView):
    """
    Vendor Location List API Class


    Example URLs:

    /api/v1/vendors/<vendor_id>/locations/
    """

    PER_PAGE = 20

    def get(self, request, vendor_id, format=None):
        """
        GET handler for Vendor Location List

        :request - HTTP request from the api call
        :vendor_id - The ID of the vendor that we want to get locations for

        In the pages meta data it will have the full resource url for you to be able
        access the next and previous pages, this should symplify the front end devs
        lives and make it easy for them to build pagination into thre components.

        Also in the meta data you can access the current amount of data returned from
        the call as well as how many items exist overall.
        """
        queryset = VendorLocation.objects.filter(vendor__pk=vendor_id).order_by('location__state', 'location__city')

        paginator = Paginator(queryset, self.PER_PAGE)

        page = request.QUERY_PARAMS.get('page', 1)

        try:
            vendor_locations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            vendor_locations = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            vendor_locations = paginator.page(paginator.num_pages)

        # check to see if we can go back 1 page
        if vendor_locations.has_previous():
            previous_page = '%s?page=%s' % (reverse('api-v1-vendor-location-list', args=[vendor_id]), int(page) - 1,)
        else:
            previous_page = None

        # check to see if we can go forward 1 page
        if vendor_locations.has_next():
            next_page = '%s?page=%s' % (reverse('api-v1-vendor-location-list', args=[vendor_id]), int(page) + 1,)
        else:
            next_page = None

        vendor_locations_serialized = VendorLocationSerializer(vendor_locations, many=True)

        # build object that we are going to return
        # with all proper meta data and information
        results = {
            'meta': {
                'pages': {
                    'previous'  : previous_page,
                    'next'      : next_page,
                    'current'   : vendor_locations.number,
                    'total'     : paginator.num_pages,
                },
                'items': {
                    'total'     : paginator.count,
                    'count'     : len(vendor_locations_serialized.data),
                    'per_page'  : self.PER_PAGE,
                    'remaining' : paginator.count - (((vendor_locations.number - 1) * self.PER_PAGE)
                                                     + len(vendor_locations_serialized.data))
                }
            },
            'results'   : vendor_locations_serialized.data
        }

        return Response(results)

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
