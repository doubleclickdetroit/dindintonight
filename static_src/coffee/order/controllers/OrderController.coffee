define [
  'BaseController'
  'ResourceService'
],
(BaseController, ResourceService) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      @order_model = new @models.order()
      ResourceService.registerOrderResource @order_model


    loadSubModules: ->
      @sandbox.require 'payment', (PaymentModule) ->
        new PaymentModule().start()


    ###*
     * Event Handlers
    ###


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @order_view = new @views.order model: @order_model

      # require sub-modules
      @loadSubModules()

      @order_view.$el


    onDestroy: ->
      @order_view.$el.remove()



  # exports
  OrderController
