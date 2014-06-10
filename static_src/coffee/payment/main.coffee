define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './views/ManagerView'
  './views/EditView'
  './views/ShowView'
],
(module, facade, BaseModule, PaymentController, ManagerView, EditView, ShowView) ->

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
          edit   : EditView
          show   : ShowView



  # register module with the facade
  facade.register 'payment', PaymentModule
