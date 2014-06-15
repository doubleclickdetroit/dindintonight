define [
  'BaseController'
  'UserService'
  'ResourceService'
],
(BaseController, UserService, ResourceService) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      @cards_collection = new @collections.cards UserService.getCards()
      ResourceService.registerPaymentResource @cards_collection

      # sandbox event listeners
      @sandbox.on 'payment:add',    @handleManagePayment, @
      @sandbox.on 'payment:edit',   @handleManagePayment, @
      @sandbox.on 'payment:cancel', @handleCancelPayment, @
      @sandbox.on 'payment:submit', @handleSubmitPayment, @


    ###*
     * Event Handlers
    ###
    handleManagePayment: (id) ->
      card_model = @cards_collection.get id
      # card_model will be undefined if `add`
      @manager_view.displayEditView card_model

    handleCancelPayment: ->
      @manager_view.displayShowView()

    handleSubmitPayment: ($form) ->
      console.log 'handleSubmitPayment', $form


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @manager_view = new @views.manager
        collection: @cards_collection

        subviews:
          edit: @views.edit
          show: @views.show

      @manager_view.render().$el

    onDestroy: ->
      @manager_view.$el.remove()



  # exports
  PaymentController
