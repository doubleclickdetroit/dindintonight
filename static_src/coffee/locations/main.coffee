define [
  'module'
  'facade'
  'BaseModule'
  './controllers/LocationsController'
  './collections/LocationsCollection'
  './models/LocationModel'
  './views/LocationsView'
],
(module, facade, BaseModule, LocationsController, LocationsCollection, LocationModel, LocationsView) ->


  class LocationsModule extends BaseModule

    controller: LocationsController

    constants: {}


    createController: (Controller) ->
      # create the controller
      @controller = new Controller
        collections:
          locations: LocationsCollection.extend
            model: LocationModel
            url  : module.config().resource_uri

        models:
          location: LocationModel

        views:
          locations: LocationsView



  # register module with the facade
  facade.register 'locations', LocationsModule
