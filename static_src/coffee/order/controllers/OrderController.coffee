define [
  'BaseController'
  'UserService'
],
(BaseController, UserService) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      # require sub-modules
      @sandbox.require 'payment', (PaymentModule) =>
        paymentModule = new PaymentModule()

        paymentModule.on 'create', ($module) =>
          @order_view.$el.append $module

        paymentModule.start()


    ###*
     * Event Handlers
    ###


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @order_view = new @views.order()
      @order_view.render().$el

    onDestroy: ->
      @order_view.$el.remove()



  # exports
  OrderController
