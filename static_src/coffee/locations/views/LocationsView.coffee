define [
  'BaseView'
  'MapService'
  'text!../templates/map.html'
],
(BaseView, MapService, tmpl_map) ->


  class LocationsView extends BaseView

    initialize: (settings={}) ->
      # initially inject the template
      @$el.html tmpl_map

      # collection listeners
      @collection.on 'sync', @render, @


    createMap: ->
      # get data to init map
      $map = @$el.find( '#map-canvas' ).get(0)

      # init map
      map_loader = MapService.createMap $map, {
        location: @collection.first().toJSON().location
      }

      # broadcast map
      map_loader.then (map_instance) =>
        @map = map_instance
        @sandbox.trigger 'map:create', map_instance


    createMarkers: ->
      locations_json = @collection.toJSON()
      MapService.addMarkers @map, locations_json


    render: ->
      if @map?
        @createMarkers()

      else
        @createMap().done => @createMarkers()

      @


    ###
      # Event Handlers
    ###



  # exports
  LocationsView
