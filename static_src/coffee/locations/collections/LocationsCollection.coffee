define [
  'backbone'
],
(Backbone) ->


  class LocationsCollection extends Backbone.Collection

    initialize: ->
      @on 'change:selected', @selectLocation, @


    parse: (response) ->
      response.results


    selectLocation: (location_model) ->
      locations = @without( location_model )
      @sandbox.util.each locations, (location) ->
        location.set 'selected', false, silent: true



  # exports
  LocationsCollection