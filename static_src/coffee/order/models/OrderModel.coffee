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

      # tack on additional attrs
      attrs.total_price = @getTotalPrice()
      attrs.has_orders  = @hasOrders()

      # return attrs as JSON
      attrs


    ###
      # Public Methods
    ###
    getTotalPrice: ->
      reduce = (memo, attrs) ->
        memo + ( parseFloat(attrs.price) * attrs.qty )

      # derrive from collection models qty attr
      @sandbox.util.reduce @get('meals'), reduce, 0

    getTotalOrders: ->
      reduce = (memo, attrs) ->
        memo += attrs.qty

      # derrive from collection models qty attr
      @sandbox.util.reduce @get('meals'), reduce, 0

    hasOrders: ->
      @getTotalOrders() > 0



  # exports
  OrderModel