define [
  'backbone'
],
(Backbone) ->


  class MealsCollection extends Backbone.Collection


    parse: (response) ->
      response.results



  # exports
  MealsCollection