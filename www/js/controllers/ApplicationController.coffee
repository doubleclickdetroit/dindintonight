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
    @locationModel   = new Models.LocationModel        events: @events
    @paymentModel    = new Models.PaymentModel         events: @events
    @mealsCollection = new Collections.MealsCollection events: @events

    # start application
    @startApplication()


  startApplication: ->
    @events.trigger 'app-ready'

    @setupListeners()
    @bootstrapData()


  setupListeners: ->
    # modesl & collections
    @mealsCollection.on 'sync',   (args...) => @events.trigger 'meals',    'reset',  @mealsCollection
    @coinModel.on       'change', (args...) => @events.trigger 'coin',     'change', @coinModel.attributes
    @locationModel.on   'change', (args...) => console.log 'location', 'change', @locationModel.attributes

    # events
    @mealsCollection.on 'change', (type, fn) =>
      total = 0

      @mealsCollection.each (meal) ->
        qty   = meal.get 'quantity'
        price = parseFloat( meal.get 'coins' ) * 10
        total += ( qty * price )

      window.total_price = total
      @events.trigger 'totalprice', total


  bootstrapData: ->
    @coinModel.fetch()
    @mealsCollection.fetch()



# exports
window.dd.Controllers.ApplicationController = ApplicationController