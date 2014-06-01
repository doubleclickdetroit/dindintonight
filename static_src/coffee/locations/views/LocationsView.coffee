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
    fillinMapLocations: (map_instance) ->
      locations_json = @collection.toJSON()
      MapService.addMarkers map_instance, locations_json


    ###
      # Event Handlers
    ###



  # exports
  LocationsView
