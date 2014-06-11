define [
  'BaseModel'
  'backbone'
],
(BaseModel, Backbone) ->


  class OrderModel extends BaseModel

    defaults:
      meals   : []
      location: null


    updateMeals: (meals_collection) ->
      @set 'meals', meals_collection


    toJSON: ->
      attrs = @attributes

      # create total_price attr
      attrs.total_price = getTotalPrice.call @, attrs.meals

      # return attrs as JSON
      attrs


    ###
      # Private Methods
    ###
    getTotalPrice = (collection) ->
      reduce = (memo, attrs) ->
        memo + ( parseFloat(attrs.price) * attrs.qty )

      # derrive from collection models qty attr
      @sandbox.util.reduce collection, reduce, 0



  # exports
  OrderModel