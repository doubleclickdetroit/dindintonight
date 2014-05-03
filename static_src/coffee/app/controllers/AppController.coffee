define [
  'BaseController'
  'stripe/main'
],
(BaseController, Stripe) ->


  class AppController extends BaseController

    initialize: (settings) ->
      $form = @sandbox.dom.find '#payment-form'
      Stripe.on 'all', -> console.log 'stripe evt', arguments
      Stripe.createToken $form



  # exports
  AppController
