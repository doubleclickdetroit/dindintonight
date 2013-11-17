# imports
Views       = window.dd.Views
Models      = window.dd.Models
Collections = window.dd.Collections



class ApplicationController

  constructor: (settings) ->
    @events = settings.events

    # cache view
    @applicationView = new Views.ApplicationView
      el    : $ 'body'
      events: @events

    # cache models & collections
    @coinModel       = new Models.CoinModel            events: @events
    @userModel       = new Models.UserModel            events: @events
    @paymentModel    = new Models.PaymentModel         events: @events
    @mealsCollection = new Collections.MealsCollection events: @events



# exports
window.dd.Controllers.ApplicationController = ApplicationController