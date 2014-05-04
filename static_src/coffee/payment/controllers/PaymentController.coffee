define [
  'BaseController'
],
(BaseController) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      # init views
      @views.payment = new @views.payment()
      @views.manage  = new @views.manage()

      # sandbox event listeners
      @sandbox.on 'manage:submit', @handleManageSubmit, @



    ###*
     * Event Handlers
    ###
    handleManageSubmit: ($form) ->
      console.log 'handleManageSubmit', $form


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @views.payment.render().$el

    onDestroy: ->
      @views.payment.$el



  # exports
  PaymentController
