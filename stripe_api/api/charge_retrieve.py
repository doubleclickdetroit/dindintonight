from django.conf import settings
import stripe

from core.api import RESTView


class ChargeRetrieve(RESTView):
    """
    Retrieve Charge API Class

    Example URLs:

    /api/v1/charges/retrieve/<id>/
    """

    def _handle_post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Charge.retrieve(kwargs.get('id'))

        return {}
