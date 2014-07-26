import hashlib
from urlparse import urlparse

from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from core.api import BadRequest, InternalRequest, MethodNotImplemented, NotAuthorized, NotFound
from core.utils import debug_print


class RESTView(APIView):
    """
    Abstract class that will be extended
    upon to build other custom Restful Views

    The developer can then override the following
    methods to enable that feature on the endpoint:

    GET         = _handle_get
    POST        = _handle_post
    PUT / PATCH = internal_put
    DELETE      = _handle_delete

    The developer must also override the URL_NAME var
    that will store the url named route that the rest
    view can use to access itself.

    If the url named route requires any extra variables
    then the developer must also override the URL_VARIABLES
    var to set the variables that are needed for the url
    """

    # Quick consts to use for cache periods
    CACHE_1_MINUTE = 60
    CACHE_15_MINUTES = 60 * 15
    CACHE_30_MINUTES = 60 * 30
    CACHE_45_MINUTES = 60 * 45
    CACHE_1_HOUR = 60 * 60 * 1
    CACHE_8_HOURS = 60 * 60 * 8
    CACHE_1_DAY = 60 * 60 * 24
    CACHE_1_WEEK = 60 * 60 * 24 * 7
    CACHE_2_WEEKS = 60 * 60 * 24 * 7 * 2
    CACHE_30_DAYS = 60 * 60 * 24 * 30
    CACHE_90_DAYS = 60 * 60 * 24 * 90
    CACHE_1_YEAR = 60 * 60 * 24 * 365
    CACHE_FOREVER = 60 * 60 * 24 * 365 * 10

    # Amount of items you want returned per page
    PER_PAGE = 20

    # the url name to this Restful Class
    URL_NAME = None

    # the url for pagination that has been overridden by a internal get call
    OVERRIDDEN_PAGINATION_URL = None

    # the url params that need to be appended to the pagination url that is being overridden
    OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS = None

    # the variables that are needed to be passed
    # along with any to build the reverse of a url
    URL_VARIABLES = None

    def internal_request(self, request, **kwargs):
        if request.method == 'GET':
            # convert the get params into a dict
            # if isinstance(request.GET, dict):
            #     query = request.GET
            # else:
            query = request.GET.dict()

            query = dict(query.items() + kwargs.items())

            try:
                user = request.user
            except Exception, e:
                user = None

            # return back a internal get
            return self.internal_get(user=user, override_pagination_url=request.path,
                                     override_pagination_query_params=request.GET, **query)
        else:
            self.raise_not_implemented()

    def get(self, request, format=None, *args, **kwargs):
        """
        Setting up generic method from Django Rest Framework
        to handle any get requests. This then passes the request
        onto our _handle_get method that (if it is implemented)
        would have to be overridden by the developer.
        """
        try:
            results = self._handle_get(request, *args, **kwargs)

            return Response(results)
        except Exception, e:
            return self._handle_exception_for_external(e)

    def internal_get(self, user=None, catalog=None, override_pagination_url=None, override_pagination_query_params=None,
                     *args, **kwargs):
        """
        Method for the developer to be able to access the
        endpoint internally and to get back the same results
        as if it was called externally. You can pass in any
        get params as if it was a external call by passing
        them into this method as KWARGS which we then will
        convert over into url params for the faked GET
        request.

        :user Current user who is making the request
        """
        # create a django http request and fake
        # that this is a get request
        django_request = HttpRequest()
        django_request.method = 'GET'
        django_request.GET = kwargs

        if catalog is not None:
            django_request.catalog = catalog

        # now we convert the django http request
        # into a django rest framework request
        # and pass in the user
        request = InternalRequest(django_request, user)

        # set the request internally to the spoofed one we just built
        self.request = request

        # check to see if the requestor wants to override the pagination url
        if override_pagination_url is not None:
            try:
                # parse the passed in url
                parsed_url = urlparse(override_pagination_url)

                new_query_string = ''

                for query_string_param in override_pagination_query_params:
                    if query_string_param != 'page':
                        new_query_string += '&{0}={1}'.format(query_string_param,
                                                              override_pagination_query_params.get(query_string_param))

                # setup the query params that were passed in
                self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS = new_query_string
                # build out the actual url minus query params
                self.OVERRIDDEN_PAGINATION_URL = parsed_url.path
            except Exception, e:
                # if by any chance the parse fails we need to revert back to the api urls
                self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS = None
                self.OVERRIDDEN_PAGINATION_URL = None

        try:
            # pass on the request and args to our get
            # handler and return the results
            return self._handle_get(request, *args)
        except Exception, e:
            self._handle_exception_for_internal(e)

    def _handle_get(self, request, *args, **kwargs):
        debug_print('Override the _handle_get to implement this method on your endpoint!', color='red')
        self.raise_not_implemented()

    def post(self, request, format=None, *args, **kwargs):
        """
        Setting up generic method from Django Rest Framework
        to handle any post requests. This then passes the request
        onto our _handle_post method that (if it is implemented)
        would have to be overridden by the developer.
        """
        try:
            results = self._handle_post(request, *args, **kwargs)

            return Response(results, status=status.HTTP_201_CREATED)
        except Exception, e:
            return self._handle_exception_for_external(e)

    def internal_post(self, user=None, catalog=None, *args, **kwargs):
        """
        Method for the developer to be able to access the
        endpoint internally and to get back the same results
        as if it was called externally. You can pass in any
        post params as if it was a external call by passing
        them into this method as KWARGS which we then will
        convert over into DATA for the faked post request.

        :user Current user who is making the request
        """
        # create a django http request and fake
        # that this is a post request
        django_request = HttpRequest()
        django_request.method = 'POST'

        if catalog is not None:
            django_request.catalog = catalog

        # now we convert the django http request
        # into a django rest framework request
        # and pass in the user and the kwargs
        request = InternalRequest(django_request, user)
        request._data = kwargs

        self.request = request

        try:
            # pass on the request and args to our post
            # handler and return the results
            return self._handle_post(request, *args)
        except Exception, e:
            self._handle_exception_for_internal(e)

    def _handle_post(self, request, *args, **kwargs):
        debug_print('Override the _handle_post to implement this method on your endpoint!', color='red')
        self.raise_not_implemented()

    def put(self, request, format=None, *args, **kwargs):
        """
        Setting up generic method from Django Rest Framework
        to handle any put requests. This then passes the request
        onto our _handle_put method that (if it is implemented)
        would have to be overridden by the developer.
        """
        try:
            results = self._handle_put(request, *args, **kwargs)

            return Response(results)
        except Exception, e:
            return self._handle_exception_for_external(e)

    def internal_put(self, user=None, catalog=None, *args, **kwargs):
        """
        Method for the developer to be able to access the
        endpoint internally and to get back the same results
        as if it was called externally. You can pass in any
        put params as if it was a external call by passing
        them into this method as KWARGS which we then will
        convert over into DATA for the faked put request.

        :user Current user who is making the request
        """
        # create a django http request and fake
        # that this is a put request
        django_request = HttpRequest()
        django_request.method = 'PUT'

        if catalog is not None:
            django_request.catalog = catalog

        # now we convert the django http request
        # into a django rest framework request
        # and pass in the user and the kwargs
        request = InternalRequest(django_request, user)
        request._data = kwargs

        self.request = request

        try:
            # pass on the request and args to our put
            # handler and return the results
            return self._handle_put(request, *args)
        except Exception, e:
            self._handle_exception_for_internal(e)

    def _handle_put(self, request, *args, **kwargs):
        """
        If you implement this method into your class
        then you will be able to also be able to use
        the PATCH method on this endpoint as we route
        all PATCH request through the PUT methods
        """
        debug_print('Override the _handle_put to implement this method on your endpoint!', color='red')
        self.raise_not_implemented()

    def patch(self, request, format=None, *args, **kwargs):
        """
        Setting up generic method from Django Rest Framework
        to handle any put requests. This then passes the request
        onto our _handle_put method that (if it is implemented)
        would have to be overridden by the developer.
        """
        try:
            results = self._handle_put(request, *args, **kwargs)

            return Response(results)
        except Exception, e:
            return self._handle_exception_for_external(e)

    def internal_patch(self, user=None, catalog=None, *args, **kwargs):
        """
        Method for the developer to be able to access the
        endpoint internally and to get back the same results
        as if it was called externally. You can pass in any
        patch params as if it was a external call by passing
        them into this method as KWARGS which we then will
        convert over into DATA for the faked put request.

        :user Current user who is making the request
        """
        try:
            return self.internal_put(user, catalog, *args, **kwargs)
        except Exception, e:
            self._handle_exception_for_internal(e)

    def delete(self, request, format=None, *args, **kwargs):
        """
        Setting up generic method from Django Rest Framework
        to handle any DELETE requests. This then passes the request
        onto our _handle_delete method that (if it is implemented)
        would have to be overridden by the developer.
        """
        # go around the circular import
        from . import APIException
        try:
            self._handle_delete(request, *args, **kwargs)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except APIException, e:
            return self._handle_exception_for_external(e)

    def internal_delete(self, user=None, catalog=None, *args, **kwargs):
        # create a django http request and fake
        # that this is a DELETE request
        django_request = HttpRequest()
        django_request.method = 'DELETE'

        if catalog is not None:
            django_request.catalog = catalog

        # now we convert the django http request
        # into a django rest framework request
        # and pass in the user and the kwargs
        request = InternalRequest(django_request, user)
        request._data = kwargs

        self.request = request

        try:
            # pass on the request and args to our post
            # handler and return the results
            return self._handle_delete(request, *args)
        except Exception, e:
            self._handle_exception_for_internal(e)

    def _handle_delete(self, request, *args, **kwargs):
        debug_print('Override the _handle_delete to implement this method on your endpoint!', color='red')
        self.raise_not_implemented()

    def _handle_exception_for_external(self, exception, *args, **kwargs):
        """
        Method to take in a exception that is being throw
        by our handler (GET, POST, PUT, PATCH, DELETE) and
        then convert that into the proper http response
        with the correct status.

        :exception The exception that was thrown
        """
        if isinstance(exception, BadRequest):
            # if the call was deemed to be a bad request
            # convert it to the proper http response
            return Response(exception.errors, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exception, NotAuthorized):
            # if the call was deemed to be not authorized
            # for the current user then we convert it to
            # the proper http response
            return Response(exception.errors, status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exception, NotFound):
            # if the call was deemed to be a invalid
            # and the item requested is not found then
            # we convert the exception to a 404
            return Response(exception.errors, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exception, PermissionDenied) or isinstance(exception, NotAuthenticated):
            # if the call was deemed to be not authorized
            # from the django rest framework due to failing
            # a permission check then we convert it to
            # the proper http response
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        elif isinstance(exception, MethodNotImplemented):
            # if the call was deemed to be not implemented
            # from the django rest framework due to the developer
            # note coding this one into the endpoint then we will
            # return a 405 since this method is not allowed
            return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            debug_print('Encountered a exception when executing your endpoint externally, the output is below!',
                        color='red')
            debug_print(exception, color='red')
            raise exception


    def _handle_exception_for_internal(self, exception, *args, **kwargs):
        """
        Method to take in a exception that is being throw
        by our handler (GET, POST, PUT, PATCH, DELETE) and
        then verify that it is a exception that can be handled
        by a python dev internally.

        :exception The exception that was thrown
        """
        if isinstance(exception, BadRequest) or isinstance(exception, NotAuthorized) \
                or isinstance(exception, NotFound) or isinstance(exception, MethodNotImplemented):
            # if the exception is a valid exception we
            # can just raise it and move on with our lives
            raise exception
        elif isinstance(exception, PermissionDenied) or isinstance(exception, NotAuthenticated):
            # if the call was deemed to be not authorized
            # from the django rest framework due to failing
            # a permission check then we convert it to
            # the proper http response
            self.raise_not_authorized()
        else:
            debug_print('Encountered a exception when executing your endpoint internally, the output is below!',
                        color='red')
            debug_print(exception, color='red')
            raise exception

    def detail_results(self, queryset, serializer):
        model_serialized = serializer(queryset)
        results = model_serialized.data
        return results


    def list_results(self, request, queryset, serializer, use_cache=False, cache_time=60 * 60 * 1, cache_version=1):
        """
        Method to create a dictionary with custom meta data
        that includes how to get the next and previous pages
        as well as how many total items / pages there are to
        the request and also how many items are left to page
        through.

        :request The request that was received through DRF
        :queryset The queryset that you are wanting to build the response for
        :serializer The serializer that you want to be used against the queryset
        :use_cache If we should use the cache or if we are going to always want fresh data
        :cache_time The time that we should cache this for in ms (Default is one hour)
        :cache_version This can be incremented as the developer changes the endpoint to make sure that the data is fresh
        """
        # param to define if we are too bust the cache
        cache_bust = False

        # placeholder for any and all additional url params
        additional_url_params = ''

        # loop over each query param and build it into the
        # additional url params
        for query_param in request.QUERY_PARAMS:
            if query_param != 'page':
                if query_param != 'cache_bust':
                    additional_url_params += '&{0}={1}'.format(query_param, request.QUERY_PARAMS.get(query_param))

            if query_param == 'cache_bust':
                debug_print('CACHE BUST!', color='green')
                cache_bust = True

        debug_print('Additional query params below', color='cyan')
        debug_print(additional_url_params, color='cyan')

        # grab the page from the query params and if
        # not passed in default to one
        page = request.QUERY_PARAMS.get('page', 1)

        results = None

        # in order to use caching you must have a URL_NAME spec'd and have the use_cache flag flipped to true
        if use_cache and self.URL_NAME is not None:
            if self.OVERRIDDEN_PAGINATION_URL is None or self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS is None:
                if self.URL_VARIABLES is None:
                    cache_url = reverse(self.URL_NAME)
                else:
                    cache_url = reverse(self.URL_NAME, kwargs=self.URL_VARIABLES)

                # build the cache name
                cache_name = 'endpoint_{0}_page_{1}_per_page_{2}_add_params_{3}_v_{4}'.format(hashlib.md5(cache_url).hexdigest(),
                    page, self.PER_PAGE, hashlib.md5(additional_url_params).hexdigest(), cache_version)
            else:
                overridden_query_params = self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS

                if overridden_query_params is None:
                    overridden_query_params = ''

                # build the cache name
                cache_name = 'endpoint_{0}_oru_{1}_oruqp_{2}_page_{3}_per_page_{4}_add_params_{5}_v_{6}'.format(
                    hashlib.md5(self.URL_NAME).hexdigest(), hashlib.md5(self.OVERRIDDEN_PAGINATION_URL).hexdigest(),
                    hashlib.md5(overridden_query_params).hexdigest(), page, self.PER_PAGE,
                    hashlib.md5(additional_url_params).hexdigest(), cache_version)

            debug_print('Cache name: "{0}"'.format(cache_name), color='yellow')

            cache_keys_name = 'endpoint_{0}_caches'.format(hashlib.md5(self.URL_NAME).hexdigest())

            debug_print('Cache keys name: "{0}"'.format(cache_keys_name), color='yellow')

            cache_keys = cache.get(cache_keys_name)

            if cache_keys is None:
                cache_keys = []

            if cache_name not in cache_keys:
                cache_keys.append(cache_name)
                cache.set(cache_keys_name, cache_keys)

            # try and get the cache if we are cache busting then we will not even try and just refresh it forcefully
            if not cache_bust:
                debug_print('LOOKING FOR CACHED RESULTS', color='yellow')
                results = cache.get(cache_name)

        if results is None:
            debug_print('FRESH FROM DB RESULTS', color='green')
            # init the pagninator with the requested page (if
            # not passed in default to 1) and the requested
            # queryset
            paginator = Paginator(queryset, self.PER_PAGE)

            try:
                models = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                models = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999),
                # deliver last page of results.
                models = paginator.page(paginator.num_pages)

            # check to see if we can go back 1 page
            if models.has_previous():
                if self.OVERRIDDEN_PAGINATION_URL is None:
                    if self.URL_VARIABLES is None:
                        url = reverse(self.URL_NAME)
                    else:
                        url = reverse(self.URL_NAME, kwargs=self.URL_VARIABLES)
                else:
                    url = self.OVERRIDDEN_PAGINATION_URL
                    additional_url_params = self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS

                previous_page = '{0}?page={1}{2}'.format(url, int(page) - 1, additional_url_params)
            else:
                previous_page = None

            # check to see if we can go forward 1 page
            if models.has_next():
                if self.OVERRIDDEN_PAGINATION_URL is None:
                    if self.URL_VARIABLES is None:
                        url = reverse(self.URL_NAME)
                    else:
                        url = reverse(self.URL_NAME, kwargs=self.URL_VARIABLES)
                else:
                    url = self.OVERRIDDEN_PAGINATION_URL
                    additional_url_params = self.OVERRIDDEN_PAGINATION_URL_QUERY_PARAMS

                next_page = '{0}?page={1}{2}'.format(url, int(page) + 1, additional_url_params)

            else:
                next_page = None

            models_serialized = serializer(models, many=True)

            # build object that we are going to return
            # with all proper meta data and information
            results = {
                'meta': {
                    'pages': {
                        'previous': previous_page,
                        'next': next_page,
                        'current': models.number,
                        'total': paginator.num_pages,
                    },
                    'items': {
                        'total': paginator.count,
                        'count': len(models_serialized.data),
                        'per_page': self.PER_PAGE,
                        'remaining': paginator.count - (((models.number - 1) * self.PER_PAGE)
                                                        + len(models_serialized.data))
                    }
                },
                'results': models_serialized.data
            }

            # if we are using the cache then we can update the cache with the new results and the cache time
            if use_cache:
                cache.set(cache_name, results, cache_time)
        else:
            debug_print('FOUND CACHED RESULTS', color='yellow')

        return results

    def bust_cache(self):
        """
        Method to bust all caches that this class may have generated
        """
        # get all cache keys for this endpoint
        cache_keys = cache.get('endpoint_{0}_caches'.format(hashlib.md5(self.URL_NAME).hexdigest()))

        # if we got back a None from redis then we have no keys
        if cache_keys is not None:
            # if we got something other than none then let's loop over each key busting it
            for cache_key in cache_keys:
                cache.delete(cache_key)


    def raise_bad_request(self, data=None, message=None):
        """
        Helper method for the developer to easily throw
        a bad request (400) exception.

        :data The data that you want returned back
        :message The message if any that you want sent back
        """
        raise BadRequest(data, message)

    def raise_not_authorized(self, data=None, message=None):
        """
        Helper method for the developer to easily throw
        a not authorized (403) exception.

        :data The data that you want returned back
        :message The message if any that you want sent back
        """
        raise NotAuthorized(data, message)

    def raise_not_found(self, data=None, message=None):
        """
        Helper method for the developer to easily throw
        a not found (404) exception.

        :data The data that you want returned back
        :message The message if any that you want sent back
        """
        raise NotFound(data, message)

    def raise_not_implemented(self):
        """
        Helper method for the developer to easily throw
        a method not implemented (405) exception.
        """
        raise MethodNotImplemented