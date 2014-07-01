define [
  'module'
  'facade'
  'BaseModule'
  './controllers/PaymentController'
  './collections/CardsCollection'
  './models/CardModel'
  './views/ManagerView'
  './views/AddView'
  './views/ShowView'
],
(module, facade, BaseModule, PaymentController, CardsCollection, CardModel, ManagerView, AddView, ShowView) ->


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
          add    : AddView
          show   : ShowView



  # register module with the facade
  facade.register 'payment', PaymentModule
