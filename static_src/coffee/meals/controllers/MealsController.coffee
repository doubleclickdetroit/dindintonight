define [
  'BaseController'
  'UserService'
],
(BaseController, UserService) ->


  class MealsController extends BaseController


    initialize: (settings) ->
      @meals_collection = new @collections.meals()
      UserService.registerMealsResource @meals_collection


    ###*
     * Event Handlers
    ###


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @meals_view = new @views.meals
        subviews:
          meal: @views.meal
        collection: @meals_collection

      @meals_view.$el

    onDestroy: ->
      @meals_view.$el.remove()



  # exports
  MealsController
