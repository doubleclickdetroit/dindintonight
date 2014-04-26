define [
  'BaseController'
],
(BaseController) ->


  class FooController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, FooController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      #

    onDestroy: ->
      #



  # exports
  FooController
