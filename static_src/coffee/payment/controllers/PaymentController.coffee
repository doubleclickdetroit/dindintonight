define [
  'BaseController'
  'ResourceService'
  'StripeService'
],
(BaseController, ResourceService, StripeService) ->


  class PaymentController extends BaseController


    initialize: (settings) ->
      @card_model       = new @models.card()
      @cards_collection = new @collections.cards()
      ResourceService.registerPaymentResource @cards_collection

      # sandbox listeners
      @sandbox.on 'payment:add',    @handleManagePayment, @
      @sandbox.on 'payment:edit',   @handleManagePayment, @
      @sandbox.on 'payment:cancel', @handleCancelPayment, @
      @sandbox.on 'payment:submit', @handleSubmitPayment, @

      # StripeService listeners
      StripeService.on 'token:success', @handleStripeAuthorization,   @
      StripeService.on 'token:failure', @handleStripeValidationError, @

      # model listeners
      @card_model.on 'invalid', @handleModelValidationError, @


    ###*
     * Event Handlers
    ###
    handleModelValidationError: (arg, error) ->
      @sandbox.trigger 'validation:error', error

    handleStripeValidationError: (error) ->
      @sandbox.trigger 'validation:error', error

    handleManagePayment: (id) ->
      card_model = @cards_collection.get id
      # card_model will be undefined if `add`
      @manager_view.displayEditView card_model

    handleCancelPayment: ->
      @manager_view.displayShowView()

    handleSubmitPayment: ($form) ->
      StripeService.createToken $form

    handleStripeAuthorization: (response) ->
      card_model = @sandbox.util.extend response.card, @card_model.toJSON()
      @cards_collection.add response, { parse: true, merge: true }


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @manager_view = new @views.manager
        model     : @card_model
        collection: @cards_collection

        subviews:
          edit: @views.edit
          show: @views.show

      @manager_view.render().$el

    onDestroy: ->
      @manager_view.$el.remove()



  # exports
  PaymentController
