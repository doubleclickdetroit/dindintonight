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
      @manager_view = new @views.manager
        subviews:
          edit: @views.edit
          show: @views.show

      @manager_view.render().$el

    onDestroy: ->
      @manager_view.$el.remove()



  # exports
  PaymentController
