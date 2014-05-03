define [
  'BaseController'
],
(BaseController) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, PaymentController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      #

    onDestroy: ->
      #



  # exports
  PaymentController
