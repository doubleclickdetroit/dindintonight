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
          @paymentModule       = new PaymentModule { id: 'payment' }
          @managePaymentModule = new PaymentModule { id: 'manager' }

          # initially start paymentModule
          @paymentModule.start()


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
