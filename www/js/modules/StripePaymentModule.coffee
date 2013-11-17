# imports



class StripePaymentModule

  constructor: (settings) ->
    @events = settings.events
    @loadScript()


  loadScript: ->
    @events.trigger 'payment-module', 'load'
    $.getScript 'https://js.stripe.com/v2', @initialize


  initialize: =>
    @events.trigger 'payment-module', 'init'



# exports
window.dd.Modules.StripePaymentModule = StripePaymentModule