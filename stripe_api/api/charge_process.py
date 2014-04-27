from core.api import RESTView
from django.conf import settings
import stripe


class ChargeProcess(RESTView):
    """
    Process Charge API Class

    Example URLs:

    /api/v1/charges/process/
    """

    def _handle_post(self, request, *args, **kwargs):
        post_data = request.DATA

        currency = post_data.get('currency', 'usd')
        amount = post_data.get('amount', None)
        card = post_data.get('card', None)  # obtained with Stripe.js
        description = post_data.get('description', None)
        errors = False
        response = {}

        if amount is None:
            response['amount'] = [
                'You must pass in an amount to be charged!',
            ]

        if card is None:
            response['card'] = [
                'You must pass in the card that was sent from Stripe!',
            ]

        if description is None:
            response['description'] = [
                'You must pass in a description for this charge!',
            ]

        if errors:
            self.raise_bad_request(response)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            card=card,
            description=description
        )

        return {}
