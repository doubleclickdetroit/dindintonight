define [
  'BaseView'
  'MapService'
  'text!../templates/map.html'
],
(BaseView, MapService, tmpl_map) ->


  class LocationsView extends BaseView

    initialize: (settings={}) ->
      # channel listeners
      @sandbox.on 'map:create', @fillinMapLocations, @


    render: ->
      @$el.html tmpl_map
      @


    ###
      # Fillin Methods
    ###
    fillinMapLocations: (map) ->
      @collection.each (location) ->
        client  = location.get 'client'
        details = location.get 'details'

        image = {
          url: 'http://placehold.it/40x40'

          # This marker is 40 pixels wide by 40 pixels tall.
          size: new google.maps.Size(40, 40)

          # The origin for this image is 0,0.
          origin: new google.maps.Point(0,0)

          # The anchor for this image is the base of the flagpole at 0,40.
          anchor: new google.maps.Point(0, 40)
        }

        coords = new google.maps.LatLng 42.335994, -83.049623

        shape = {
          type: 'poly',
          coords: [1, 1, 1, 20, 18, 20, 18 , 1]
        }

        new google.maps.Marker
          position: coords
          map     : map
          icon    : image
          shape   : shape
          title   : client.name
          zIndex  : 1


    ###
      # Event Handlers
    ###



  # exports
  LocationsView
