define [
  'BaseView'
  'MapService'
  'hbs!../templates/map'
  'hbs!../templates/overlay'
],
(BaseView, MapService, hbs_map, hbs_overlay) ->


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
      serving_area = @collection.first().toJSON().serving_area
      serving_area.click = -> console.log 'map evt', arguments

      # init map with map default position
      map_loader = MapService.createMap $map, serving_area

      # broadcast map
      map_loader.then (map_instance) =>
        @map = map_instance
        @sandbox.trigger 'map:create', map_instance


    createMarkers: ->
      @collection.each (location_model) =>
        location_json = location_model.toJSON()
        console.log location_model.attributes
        location_html = hbs_overlay location_json

        options = @sandbox.util.extend location_json, {
          details: location_json
          content: location_html
          click: -> console.log 'yo', arguments
        }

        MapService.addMarker @map, options


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
