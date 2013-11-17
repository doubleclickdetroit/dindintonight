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

    # start application
    @startApplication()


  startApplication: ->
    @events.trigger 'app-ready'

    # @events.on 'coin',  (coin)  => console.log 'coin event',  coin
    # @events.on 'meals', (meals) => console.log 'meals event', meals

    @setupListeners()
    @bootstrapData()


  setupListeners: ->
    @coinModel.on       'change', (args...) => @events.trigger 'coin', 'change', @coinModel.attributes
    @mealsCollection.on 'sync',   (args...) => @events.trigger 'meals', 'reset', @mealsCollection.toJSON()


  bootstrapData: ->
    @coinModel.fetch()
    @mealsCollection.fetch()



# exports
window.dd.Controllers.ApplicationController = ApplicationController