define [
  'BaseController'
  'ResourceService'
],
(BaseController, ResourceService) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      @order_model = new @models.order()
      ResourceService.registerOrderResource @order_model

      # listeners
      @sandbox.on 'submit', @handleOrderSubmit, @

      # ResourceService listeners
      ResourceService.view_manager.on 'change:order', @handleVisibilityToggle, @

    loadSubModules: ->
      @sandbox.require 'payment', (PaymentModule) ->
        new PaymentModule().start()


    ###*
     * Event Handlers
    ###
    handleVisibilityToggle: (attrs, is_visible) ->
      @order_view.toggle is_visible

    handleOrderSubmit: (evt) ->
      @order_model.save()


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @order_view = new @views.order model: @order_model

      # require sub-modules
      @loadSubModules()

      @order_view.hide()

    onDestroy: ->
      @order_view.$el.remove()



  # exports
  OrderController
