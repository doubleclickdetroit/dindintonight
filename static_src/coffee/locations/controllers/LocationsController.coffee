define [
  'BaseController'
],
(BaseController) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @

      # init views
      @views.locations = new @views.locations()


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, LocationsController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.locations.render().$el

    onDestroy: ->
      @views.locations.$el



  # exports
  LocationsController
