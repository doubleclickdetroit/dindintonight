define [
  'BaseController'
  'UserService'
],
(BaseController, UserService) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      # init views
      @views.order = new @views.order()

      # require sub-modules
      @sandbox.on 'create', =>
        @sandbox.require 'payment', (PaymentModule) =>
          @paymentModule = new PaymentModule()
          @paymentModule.start()
          setTimeout (=>@paymentModule.stop()), 3000
          setTimeout (=>@paymentModule.start()), 6000


    ###*
     * Event Handlers
    ###


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.order.render().$el

    onDestroy: ->
      @views.order.$el



  # exports
  OrderController
