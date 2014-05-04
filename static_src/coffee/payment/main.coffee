define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './views/PaymentView'
  './views/ManageView'
],
(module, facade, BaseModule, PaymentController, PaymentView, ManageView) ->


  class PaymentModule extends BaseModule

    controller: PaymentController

    constants: {}


    initialize: ->
      #


    createController: (Controller) ->
      console.log '*** createController', arguments

      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        views:
          payment: PaymentView
          manage : ManageView



  # register module with the facade
  facade.register 'payment', PaymentModule
