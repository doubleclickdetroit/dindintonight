from rest_framework.request import Request


class InternalRequest(Request):
    """
    Class that is used for any internal
    requests to a Django Rest Framework
    endpoint
    """

    # the forced in user from the init
    _forced_user = None

    def __init__(self, request, user=None, parsers=None, authenticators=None,
                 negotiator=None, parser_context=None):
        """
        Method to init the class and has been modified to
        allow the developer to pass a user in that will
        then be listed as the forced user. The forced user
        is then later used as the overridden user properties
        returned value.
        """
        self._forced_user = user
        self._user = user
        super(InternalRequest, self).__init__(request, parsers, authenticators,
                                              negotiator, parser_context)

    @property
    def user(self):
        """
        Overridden property to allow access to the passed
        in user (forced_user) from the init of the class
        """
        return self._forced_user
