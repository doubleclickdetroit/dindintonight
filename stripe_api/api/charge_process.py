from django.conf import settings
import stripe

from core.api import RESTView
from meals.models import Meal
from users.models import User, UserMealPurchaseHistory


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
        meals = post_data.get('meals', None)
        user = post_data.get('user', None)

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

        if user is not None:
            try:
                user = User.objects.get(pk=user.get('id'))
            except User.DoesNotExist:
                response['user'] = [
                    'Invalid user requested'
                ]

        if meals is None:
            response = {
                'meals': ['Meals is required!']
            }
            self.raise_bad_request(response)
        else:
            # setup the error response object
            meals_errors = []

            # loop over the meals trying to make sure that all meals exist and can be charged
            for meal in meals:
                try:
                    Meal.objects.get(pk=meal.get('id'), is_deleted=False)
                except Meal.DoesNotExist:
                    # if we cannot get the meal then we will add it to the list of bad meals
                    meals_errors.append('Meal with the id of {0} doesn\'t exist!'.format(meal.id))

            # if we have bad meals then we can throw a 400 for bad request
            if meals_errors.count() > 0:
                response['meals'] = meals_errors

        if errors:
            self.raise_bad_request(response)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            card=card,
            description=description
        )

        users_meal_purchase_history = []

        for meal in meals:
            meal = Meal.objects.get(pk=meal.get('id'), is_deleted=False)
            user_meal_purchase_history = UserMealPurchaseHistory()
            user_meal_purchase_history.user = user
            user_meal_purchase_history.meal = meal
            user_meal_purchase_history.save()
            users_meal_purchase_history.append(user_meal_purchase_history)

        return charge
