define [
  'BaseView'
  'MapService'
  'hbs!../templates/map'
],
(BaseView, MapService, hbs_map) ->


  class LocationsView extends BaseView

    initialize: (settings={}) ->
      # initially inject the template
      @$el.html hbs_map( title: 'LocationsView' )

      # collection listeners
      @collection.on 'sync', @render, @


    createMap: ->
      # get data to init map
      $map = @$el.find( '#map-canvas' ).get(0)

      # default to city view of first location
      location = @collection.first().toJSON().location

      # init map with map default position
      map_loader = MapService.createMap $map, location

      # broadcast map
      map_loader.then (map_instance) =>
        @map = map_instance
        @sandbox.trigger 'map:create', map_instance


    createMarkers: ->
      locations_json = @collection.toJSON()
      MapService.addMarkers @map, locations_json


    render: ->
      # collection n'sync, add the markers
      if @map?
        @createMarkers()

      # if needed, create the map and add markers
      else
        @createMap().done => @createMarkers()

      setTimeout (=>
        location_id = @collection.first().get 'id'
        @sandbox.trigger 'location:selected', location_id
      ), 5000

      @


    ###
      # Event Handlers
    ###



  # exports
  LocationsView
