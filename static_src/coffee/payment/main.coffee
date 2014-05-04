define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './views/PaymentView'
],
(module, facade, BaseModule, PaymentController, PaymentView) ->


  class PaymentModule extends BaseModule

    controller: PaymentController

    constants:
      GREETING: 'Why, hello there'


    initialize: ->
      #


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        views:
          payment: PaymentView

      # welcome the newly initialized controller
      @trigger 'controller:welcome', @constant().GREETING



  # register module with the facade
  facade.register 'payment', PaymentModule
