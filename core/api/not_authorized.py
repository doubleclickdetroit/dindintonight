from . import APIException


class NotAuthorized(APIException):
    """
    Equivalent of throwing a 403
    """
    pass