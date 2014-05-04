define [
  'module'
  'facade'
  'BaseModule'
  './controllers/LocationsController'
  './views/LocationsView'
],
(module, facade, BaseModule, LocationsController, LocationsView) ->


  class LocationsModule extends BaseModule

    controller: LocationsController

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
          locations: LocationsView

      # welcome the newly initialized controller
      @trigger 'controller:welcome', @constant().GREETING



  # register module with the facade
  facade.register 'locations', LocationsModule
