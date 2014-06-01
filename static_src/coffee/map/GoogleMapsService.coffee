define [
  'facade'
],
(facade) ->


  class GoogleMapsService

    __api = google.maps

    constructor: ->
      @defaults =
        zoom: 18


    createMap: ($map, settings={}) ->
      options = facade.util.extend {}, settings, @defaults
      new __api.Map $map, options


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


    createBounds: ->
      new __api.LatLngBounds()


    createCoords: (lat, lng) ->
      new __api.LatLng lat, lng


    createMarker: (options={}) ->
      settings =
        title : ''
        location:
          lat: 42.335994
          lng: -83.049623
        image:
          url     : 'http://placehold.it/40x40'
          width   : 40
          height  : 40
          origin_x: 0
          origin_y: 0
          anchor_x: 0
          anchor_y: 40
        shape:
          type  : 'poly'
          coords: [1, 1, 1, 20, 18, 20, 18 , 1]
        zIndex: 1

      # deep extend settings
      facade.util.extend true, settings, options

      # reassign values
      facade.util.extend true, settings, {
        location: @createCoords settings.location.lat, settings.location.lng
        image:
          size  : __api.Size  settings.image.width,    settings.image.height
          origin: __api.Point settings.image.origin_x, settings.image.origin_y
          anchor: __api.Point settings.image.anchor_x, settings.image.anchor_y
      }

      # return marker
      new __api.Marker
        position: settings.location
        icon    : settings.image
        shape   : settings.shape
        title   : settings.title
        zIndex  : settings.zIndex


    addMarkers: (map_instance, collection) ->
      bounds = @createBounds()

      facade.util.each collection, (settings) =>

        # create the marker and add to the map
        marker = @createMarker settings
        marker.setMap map_instance

        # extend the bounds to include each marker's position
        bounds.extend marker.position

      # fit the map to the newly inclusive bounds
      map_instance.fitBounds bounds



  # exports
  GoogleMapsService