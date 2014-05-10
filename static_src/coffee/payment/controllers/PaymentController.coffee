define [
  'BaseController'
],
(BaseController) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      # sandbox event listeners
      @sandbox.on 'payment:submit', @handleManageSubmit, @



    ###*
     * Event Handlers
    ###
    handleManageSubmit: ($form) ->
      console.log 'handleManageSubmit', $form


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @selected_view = new @views.selected()
      console.log 'Controller', @selected_view
      @selected_view.render().$el

    onDestroy: ->
      @selected_view.$el.remove()



  # exports
  PaymentController
