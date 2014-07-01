define [
  'BaseModel'
  'backbone'
],
(BaseModel, Backbone) ->


  class OrderModel extends BaseModel

    urlRoot: '/api/v1/charges/process/'

    defaults:
      meals   : []
      user    : null
      card    : null
      location: null


    updateUser: (user_model) ->
      @set 'user', user_model

    updateMeals: (meals_collection=[]) ->
      @set 'meals', meals_collection

    updateCard: (card_model=null) ->
      @set 'card', card_model

    updateLocation: (location_model=null) ->
      @set 'location', location_model

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