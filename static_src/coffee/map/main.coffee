define [
  'facade'
  'BaseService'
  './map/GoogleMapsService'
],
(facade, BaseService, GoogleMapsService) ->


  class MapService extends BaseService

    __api = new GoogleMapsService()

    constants: {}


    initialize: ->
      #


    createMap: ($map, settings) ->
      d = @util.deferred()

      # check for location
      location = settings?.location || {}

      # determine type of location
      if location.address?
        q = __api.geocodeAddress( location.address ).then (response) ->
          settings.center = response.coords

      else if location.lat? and location.lng?
        q = __api.geocodeCoords( location.lat, location.lng ).then (response) ->
          settings.center = response.coords

      else
        q = facade.util.deferred().resolve().promise()

      # when location is determined, create map
      q.done ->
        map = __api.createMap $map, settings
        d.resolve map

      # return promise
      d.promise()


    addMarkers: (map_instance, locations_collection) ->
      __api.addMarkers map_instance, locations_collection



  # Register service
  facade.register 'map', MapService