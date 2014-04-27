from core.api import RESTView
from django.conf import settings
import stripe
from users.models import User, UserStripeCard
from users.serializers import UserStripeCardSerializer


class CardList(RESTView):
    """
    Card List API Class

    Example URLs:

    /api/v1/users/<user_id>/cards/
    """

    URL_NAME = 'api-v1-user-cards-list'

    def _handle_get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs.get('user_id'))
        except User.DoesNotExist:
            self.raise_not_found()

        self.URL_VARIABLES = {
            'user_id': kwargs.get('user_id')
        }

        return self.list_results(request, user.cards.all(), UserStripeCardSerializer, use_cache=True,
                                 cache_time=self.CACHE_30_DAYS, cache_version=1)

    def _handle_post(self, request, *args, **kwargs):
        post_data = request.DATA

        if post_data.get('card', None) is None:
            response = {
                'card': [
                    'You must pass in the card that was sent from Stripe!',
                ]
            }
            self.raise_bad_request(response)

        try:
            user = User.objects.get(pk=kwargs.get('user_id'))
        except User.DoesNotExist:
            self.raise_not_found()

        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer = stripe.Customer.retrieve(user.customer.customer_id)
        card = customer.cards.create(card=post_data.get('card'))

        user_stripe_card = UserStripeCard()
        user_stripe_card.user = user
        user_stripe_card.card_id = card.id
        user_stripe_card.name = card.name
        user_stripe_card.description = post_data.get('description', '')
        user_stripe_card.last4 = card.last4
        user_stripe_card.type = card.type
        user_stripe_card.expiration_month = card.exp_month
        user_stripe_card.expiration_year = card.exp_year
        user_stripe_card.fingerprint = card.fingerprint
        user_stripe_card.country = card.country
        user_stripe_card.save()

        return self.detail_results(user_stripe_card, UserStripeCardSerializer)
