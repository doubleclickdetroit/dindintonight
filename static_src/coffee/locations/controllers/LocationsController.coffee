define [
  'BaseController'
],
(BaseController) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      # console?.log "#{greeting}, LocationsController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @locations_view = new @views.locations()
      @locations_view.render().$el

    onDestroy: ->
      @locations_view.$el.remove()



  # exports
  LocationsController
