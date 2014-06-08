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


    createMap: ($map, settings={}) ->
      d = @util.deferred()

      # determine type of location
      if settings.address?
        q = __api.geocodeAddress( settings.address ).then (response) ->
          facade.util.extend settings, response.coords
      else
        q = facade.util.deferred().resolve().promise()


      # when location is determined, create map
      q.done ->
        map = __api.createMap $map, settings
        d.resolve map

      # return promise
      d.promise()


    addMarker: (map_instance, options) ->
      __api.addMarker map_instance, options


    addMarkers: (map_instance, locations_collection) ->
      __api.addMarkers map_instance, locations_collection



  # Register service
  facade.register 'map', MapService