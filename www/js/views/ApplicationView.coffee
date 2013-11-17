# imports
Views  = window.dd.Views


class ApplicationView extends Views.BaseView

  initialize: (settings) ->
    @events = settings.events

    # setup subviews
    @setupSubviews()

    # cache template
    settings.template = @$ '#tmpl-alert'

    # listners
    @events.on 'app', @handleAppEvent, @

    # call to super
    super


  render: (response) ->
    $alert = $( @tmpl response )
    $alert.appendTo @$el
    $alert.animate { bottom:0 }, 'slow'

    setTimeout (-> $alert.fadeOut( 'slow', -> $alert.remove() ) ), 3000


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


  ### Event Handlers ###
  handleAppEvent: (type, text, link) ->
    if type in ['error', 'success']
      type = 'danger' if type is 'error'
      @render 'type': type, 'text': text, 'link': link




# exports
window.dd.Views.ApplicationView = ApplicationView