define [
  'backbone'
],
(Backbone) ->


  class LocationsCollection extends Backbone.Collection


    parse: (response) ->
      response.results


    selectLocation: (location_id) ->
      @each (location) ->
        is_location = location_id is location.attributes.id
        location.set 'selected', is_location, silent: !is_location



  # exports
  LocationsCollection