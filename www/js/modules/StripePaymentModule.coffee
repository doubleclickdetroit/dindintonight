# imports
Views       = window.dd.Views
Models      = window.dd.Models
Collecitons = window.dd.Collecitons



class StripePaymentModule

  constructor: ->
    console.log 'StripePaymentModule instantiated'
    @loadScript()


  loadScript: ->
    $.getScript 'https://js.stripe.com/v2', @initialize



# exports
window.dd.Modules.StripePaymentModule = StripePaymentModule