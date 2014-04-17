class APIException(Exception):
    """
    Abstract class that will be extended
    upon to build other custom API Exceptions
    that could be thrown by the RESTView class
    """

    def __init__(self, errors=None, message=None):
        self.errors = errors
        self.message = message
