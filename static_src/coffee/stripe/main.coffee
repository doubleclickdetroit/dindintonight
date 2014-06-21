define [
  'facade'
  'BaseService'
  'stripe_api'
],
(facade, BaseService, Stripe) ->


  class StripeService extends BaseService

    constants:
      PUBLISHABLE_KEY: 'pk_test_3NyGXdUaWYpsRacIxKN0ndr8'


    initialize: ->
      # identify our website
      Stripe.setPublishableKey @constant().PUBLISHABLE_KEY


    createToken: ($form) ->
      Stripe.card.createToken $form, @handleCreateTokenResponse


    ###
      # Event Handlers
    ###
    handleCreateTokenResponse: (status, response) =>
      if response.error
        # broadcast the errors
        @trigger 'token:failure', response.error.message

      else
        # token contains id, last4, and card type
        @trigger 'token:success', response



  # Register service
  facade.register 'stripe', StripeService