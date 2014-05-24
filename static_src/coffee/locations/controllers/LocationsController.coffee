define [
  'BaseController'
  'MapService'
],
(BaseController, MapService) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      @locations_collection = new @collections.locations()

      # know when the view is loaded
      view_loader = @sandbox.util.deferred()
      @sandbox.on 'create', view_loader.resolve, @

      # fetch locations and then use to populate the @locations_view
      @sandbox.util.when( view_loader.promise(), @locations_collection.fetch() )
      .done @initMapServiceLocationView


    initMapServiceLocationView: =>
      # get data to init map
      $map     = @locations_view.$el.find '#map-canvas'
      location = @locations_collection.first().toJSON().location

      # init map
      map_loader = MapService.createMap $map.get(0), {
        location: lat: location.latitude, lng: location.longitude
      }

      # broadcast map
      map_loader.done (map) =>
        @sandbox.trigger 'map:create', map


    ###*
     * Event Handlers
    ###


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @locations_view = new @views.locations
        collection: @locations_collection

      @locations_view.render().$el

    onDestroy: ->
      @locations_view.$el.remove()



  # exports
  LocationsController
