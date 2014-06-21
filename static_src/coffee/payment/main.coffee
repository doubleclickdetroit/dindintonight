define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './collections/CardsCollection'
  './models/CardModel'
  './views/ManagerView'
  './views/EditView'
  './views/ShowView'
],
(module, facade, BaseModule, PaymentController, CardsCollection, CardModel, ManagerView, EditView, ShowView) ->


  class PaymentModule extends BaseModule

    controller: PaymentController

    constants: {}


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        collections:
          cards: CardsCollection.extend { model: CardModel }

        models:
          card: CardModel

        views:
          manager: ManagerView
          edit   : EditView
          show   : ShowView



  # register module with the facade
  facade.register 'payment', PaymentModule
