define [
  'BaseController'
  'ResourceService'
],
(BaseController, ResourceService) ->


  class MealsController extends BaseController


    initialize: (settings) ->
      @meals_collection = new @collections.meals()
      ResourceService.registerMealsResource @meals_collection

      # ResourceService listeners
      ResourceService.view_manager.on 'change:meals', @handleVisibilityToggle, @


    ###*
     * Event Handlers
    ###
    handleVisibilityToggle: (attrs, is_visible) ->
      @meals_view.toggle is_visible


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @meals_view = new @views.meals
        subviews:
          meal: @views.meal
        collection: @meals_collection

      @meals_view.hide()

    onDestroy: ->
      @meals_view.$el.remove()



  # exports
  MealsController
