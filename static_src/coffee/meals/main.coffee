define [
  'module'
  'facade'
  'BaseModule'
  './controllers/MealsController'
  './collections/MealsCollection'
  './models/MealModel'
  './views/MealsView'
  './views/MealView'
],
(module, facade, BaseModule, MealsController, MealsCollection, MealModel, MealsView, MealView) ->


  class MealsModule extends BaseModule

    controller: MealsController

    constants: {}


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        # bootstrap with module data
        bootstrap: module.config()
        # references
        collections:
          meals: MealsCollection.extend
            model: MealModel

        models:
          meal: MealModel

        views:
          meals: MealsView
          meal : MealView



  # register module with the facade
  facade.register 'meals', MealsModule
