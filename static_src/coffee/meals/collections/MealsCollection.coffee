define [
  'backbone'
],
(Backbone) ->


  class MealsCollection extends Backbone.Collection


    parse: (response) ->
      response.results


    ###
      # Public Methods
    ###
    getOrderedMeals: ->
      qtyFilter = (attrs) -> attrs.qty > 0
      @sandbox.util.filter @toJSON(), qtyFilter



  # exports
  MealsCollection