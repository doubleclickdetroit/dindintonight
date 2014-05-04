define [
  'module'
  'facade'
  'BaseModule'
  './controllers/OrderController'
  './views/OrderView'
],
(module, facade, BaseModule, OrderController, OrderView) ->


  class OrderModule extends BaseModule

    controller: OrderController

    constants: {}


    initialize: ->
      #


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        views:
          order: OrderView



  # register module with the facade
  facade.register 'order', OrderModule
