from . import APIException


class MethodNotImplemented(APIException):
    """
    Equivalent of throwing a 405
    """
    pass