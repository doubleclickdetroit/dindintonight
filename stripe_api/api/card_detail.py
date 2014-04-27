from django.conf import settings
from core.api import RESTView
from users.models import UserStripeCard
from users.serializers import UserStripeCardSerializer
import stripe


class CardDetail(RESTView):
    """
    Card Detail API Class

    Example URLs:

    /api/v1/users/<user_id>/cards/<pk>/
    """
    def get_object(self, pk, user_id):
        """
        Method to ease access of getting the queryset for use

        :pk - PK of the location that you want to get detail on
        :user_id -
        """
        try:
            return UserStripeCard.objects.get(pk=pk, user__pk=user_id)
        except UserStripeCard.DoesNotExist:
            self.raise_not_found()

    def _handle_get(self, request, *args, **kwargs):
        """
        GET handler for Card Detail

        :request - HTTP request from the api call
        :pk - PK of the location that you want to get detail on
        :user_id -
        """
        card = self.get_object(kwargs.get('pk'), kwargs.get('user_id'))

        return self.detail_results(card ,UserStripeCardSerializer)

    def _handle_delete(self, request, *args, **kwargs):
        card = self.get_object(kwargs.get('pk'), kwargs.get('user_id'))

        stripe.api_key = settings.STRIPE_SECRET_KEY
        customer = stripe.Customer.retrieve(card.user.customer.customer_id)
        customer.cards.retrieve(card.card_id).delete()

        card.delete()
