# imports



class StripePaymentModule

  instance = null
  API_KEY_PUB  = 'pk_live_izwf8ccnTN4Sy7KCKwr1Qui5'
  API_KEY_DEMO = 'pk_test_7bJDaUT5cCrT6y8vPBb8VB14'


  constructor: (settings) ->
    instance = @
    @events  = settings.events
    @loadScript()

    # listeners
    @events.on 'process-payment', processCreditCardPayment


  loadScript: ->
    @events.trigger 'payment-module', 'load'
    $.getScript 'https://js.stripe.com/v2', @initialize


  initialize: =>
    Stripe.setPublishableKey API_KEY_DEMO
    @events.trigger 'payment-module', 'init'


  ### Private Methods ###
  validateCardNumber = (cc_number) ->
    @Stripe.card.validateCardNumber cc_number


  validateExpiry = (month, year) ->
    @Stripe.card.validateExpiry month, year


  validateCVC = (cvc) ->
    @Stripe.card.validateExpiry cvc


  processCreditCardPayment = (cc_data) ->
    Stripe.card.createToken cc_data, handleCreditCardPayment


  handleCreditCardPayment = (status, response) ->
    if response.error
      instance.events.trigger 'payment-module', 'error', response.error.message
    else
      instance.events.trigger 'payment-module', 'token', response



# exports
window.dd.Modules.StripePaymentModule = StripePaymentModule