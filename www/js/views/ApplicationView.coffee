# imports
Views = window.dd.Views



class ApplicationView extends Views.BaseView

  initialize: (settings) ->
    @events = settings.events

    # setup subviews
    @setupSubviews()


  render: ->


  setupSubviews: ->
    @mealsView = new Views.MealsView
      events  : @events
      el      : @$ '#view-meals'
      template: @$ '#tmpl-meal'

    @locationView = new Views.LocationView
      events  : @events
      el      : @$ '#view-location'

    @paymentView = new Views.PaymentView
      events  : @events
      el      : @$ '#view-payment'
      template: @$ '#tmpl-payment'




# exports
window.dd.Views.ApplicationView = ApplicationView