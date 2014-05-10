define [
  'BaseController'
],
(BaseController) ->


  class MealsController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      # console?.log "#{greeting}, MealsController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @meals_view = new @views.meals()
      @meals_view.render().$el

    onDestroy: ->
      @meals_view.$el.remove()



  # exports
  MealsController
