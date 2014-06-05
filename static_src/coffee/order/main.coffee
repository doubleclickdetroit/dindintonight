define [
  'module'
  'facade'
  'BaseModule'
  './controllers/OrderController'
  './models/OrderModel'
  './views/OrderView'
],
(module, facade, BaseModule, OrderController, OrderModel, OrderView) ->


  class OrderModule extends BaseModule

    controller: OrderController

    constants: {}


    initialize: ->
      #

    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # references
        models:
          order: OrderModel

        views:
          order: OrderView



  # register module with the facade
  facade.register 'order', OrderModule
