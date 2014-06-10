define [
  'BaseController'
  'ResourceService'
],
(BaseController, ResourceService) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      @order_model = new @models.order()
      ResourceService.registerOrderResource @order_model

      # require sub-modules
      @loadSubModules()

    loadSubModules: ->
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
      @order_view.$el

    onDestroy: ->
      @order_view.$el.remove()



  # exports
  OrderController
