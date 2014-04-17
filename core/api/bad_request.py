from . import APIException


class BadRequest(APIException):
    """
    Equivalent of throwing a 400
    """
    pass