# imports
Views = window.dd.Views



class ApplicationView extends Views.BaseView

  initialize: (settings) ->
    @events = settings.events

    # setup subviews
    @setupSubviews()


  render: ->


  setupSubviews: ->
    @menuView     = new Views.MenuView     events: @events
    @locationView = new Views.LocationView events: @events
    @paymentView  = new Views.PaymentView  events: @events



# exports
window.dd.Views.ApplicationView = ApplicationView