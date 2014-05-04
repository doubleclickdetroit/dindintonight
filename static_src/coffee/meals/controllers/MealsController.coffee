define [
  'BaseController'
],
(BaseController) ->


  class MealsController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @

      # init views
      @views.meals = new @views.meals()


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, MealsController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.meals.render().$el

    onDestroy: ->
      @views.meals.$el



  # exports
  MealsController
