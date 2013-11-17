# imports
Modules     = window.dd.Modules
Controllers = window.dd.Controllers



# DOM Ready
$ ->
  # events
  mediator = _.extend {}, Backbone.Events

  # instantiate modules & controllers
  applicationController = new Controllers.ApplicationController events: mediator
  stripePaymentModule   = new Modules.StripePaymentModule       events: mediator