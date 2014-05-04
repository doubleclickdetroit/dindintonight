define [
  'module'
  'facade'
  'BaseModule'
  './controllers/MealsController'
  './views/MealsView'
],
(module, facade, BaseModule, MealsController, MealsView) ->


  class MealsModule extends BaseModule

    controller: MealsController

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
          meals: MealsView

      # welcome the newly initialized controller
      @trigger 'controller:welcome', @constant().GREETING



  # register module with the facade
  facade.register 'meals', MealsModule
