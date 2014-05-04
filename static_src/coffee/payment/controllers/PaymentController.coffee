define [
  'BaseController'
],
(BaseController) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @

      # init views
      @views.payment = new @views.payment()


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, PaymentController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.payment.render().$el

    onDestroy: ->
      @views.payment.$el



  # exports
  PaymentController
