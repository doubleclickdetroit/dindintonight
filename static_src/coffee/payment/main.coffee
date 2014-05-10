define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './factories/ViewFactory'
],
(module, facade, BaseModule, PaymentController, ViewFactory) ->


  class PaymentModule extends BaseModule

    controller: PaymentController

    constants: {}


    initialize: (settings) ->
      # set selected view
      @selected_view = ViewFactory settings.id


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        views:
          selected: @selected_view



  # register module with the facade
  facade.register 'payment', PaymentModule
