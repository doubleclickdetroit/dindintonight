define [
  'backbone'
],
(Backbone) ->


  class LocationsCollection extends Backbone.Collection


    parse: (response) ->
      response.results



  # exports
  LocationsCollection