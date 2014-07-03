define [
  'BaseModel'
],
(BaseModel) ->


  class OrderModel extends BaseModel

    urlRoot: '/api/v1/charges/process/'

    defaults:
      meals   : []
      user    : null
      card    : null
      location: null


    validate: (attrs) ->
      is_valid = @isLocationValid() and @isMealsValid() and @isCardValid()
      'Please correct errors.' unless is_valid


    ###
      # Internal Methods
    ###
    updateUser: (user_model) ->
      @set 'user', user_model

    updateMeals: (meals_collection=[]) ->
      @set 'meals', meals_collection

    updateCard: (card_model=null) ->
      @set 'card', card_model

    updateLocation: (location_model=null) ->
      @set 'location', location_model


    ###
      # Public Methods
    ###
    isLocationValid: ->
      @get( 'location' )?

    isMealsValid: ->
      @get( 'meals' ).length > 0

    isCardValid: ->
      @get( 'card' )?

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