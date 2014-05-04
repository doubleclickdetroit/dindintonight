define [
  'BaseController'
],
(BaseController) ->


  class OrderController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'controller:welcome', @handleControllerWelcome, @

      # init views
      @views.order = new @views.order()


    ###*
     * Event Handlers
    ###
    handleControllerWelcome: (greeting) ->
      console?.log "#{greeting}, OrderController!", @bootstrap


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.order.render().$el

    onDestroy: ->
      @views.order.$el



  # exports
  OrderController
