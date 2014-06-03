define [
  'BaseController'
],
(BaseController) ->


  class MealsController extends BaseController


    initialize: (settings) ->
      @meals_collection = new @collections.meals()

      # sandbox event listeners
      @sandbox.on 'resource:uri', @handleUpdatingCollectionUri, @


    ###*
     * Event Handlers
    ###
    handleUpdatingCollectionUri: (resource_uri) ->
      @meals_collection.url = resource_uri
      @meals_collection.fetch()


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @meals_view = new @views.meals
        subviews:
          meal: @views.meal
        collection: @meals_collection

      @meals_view.render().$el


    onDestroy: ->
      @meals_view.$el.remove()



  # exports
  MealsController
