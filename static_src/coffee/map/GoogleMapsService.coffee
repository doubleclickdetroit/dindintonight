define [
  'facade'
],
(facade) ->


  class GoogleMapsService

    __api = google.maps

    constructor: ->
      @defaults =
        zoom: 18


    geocodeAddress: (address) ->
      q = facade.util.deferred()

      @createGeocode( address: address ).done (results, status) ->
        if (status == google.maps.GeocoderStatus.OK)
          q.resolve { address: address, coords: results[0].geometry.location }
        else
          q.reject { error: "Geocode was not successful for the following reason #{status}" }

      q.promise()


    geocodeCoords: (lat, lng) ->
      q = facade.util.deferred()

      coords = @createCoords lat, lng
      @createGeocode( latLng: coords ).done (results, status) ->
        return q.resolve({ address: results[1], coords: coords }) if results[1]?
        q.reject({ error: "Geocoder failed due to #{status}" })

      q.promise()


    createGeocode: (position) ->
      q = facade.util.deferred()

      geocoder = new __api.Geocoder()
      geocoder.geocode position, q.resolve

      q.promise()


    createCoords: (lat, lng) ->
      new __api.LatLng lat, lng


    createMap: ($map, settings={}) ->
      options = facade.util.extend {}, settings, @defaults
      new __api.Map $map, options



  # exports
  GoogleMapsService