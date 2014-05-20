define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './views/ManagerView'
],
(module, facade, BaseModule, PaymentController, ManagerView) ->


  class PaymentModule extends BaseModule

    controller: PaymentController

    constants: {}


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        views:
          manager: ManagerView



  # register module with the facade
  facade.register 'payment', PaymentModule
