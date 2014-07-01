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
      @sandbox.on 'payment:add',    @handleAddPayment,    @
      @sandbox.on 'payment:remove', @handleRemovePayment, @
      @sandbox.on 'payment:select', @handleSelectPayment, @
      @sandbox.on 'payment:cancel', @handleCancelPayment, @
      @sandbox.on 'payment:submit', @handleSubmitPayment, @

      # StripeService listeners
      StripeService.on 'token:success', @handleStripeAuthorization,   @
      StripeService.on 'token:failure', @handleStripeValidationError, @

      # model listeners
      @card_model.on 'invalid', @handleModelValidationError, @


    addPayment: (card_model) ->
      @cards_collection.add card_model, { parse: true, merge: true }

      if @cards_collection.length is 1
        @selectPayment @cards_collection.first()

    removePayment: (card_model) ->
      console.log 'removePayment', card_model
      card_model?.destroy()

    selectPayment: (card_model) ->
      card_model.set 'selected', true


    ###*
     * Event Handlers
    ###
    handleModelValidationError: (arg, error) ->
      @sandbox.trigger 'validation:error', error

    handleStripeValidationError: (error) ->
      @sandbox.trigger 'validation:error', error

    handleAddPayment: ->
      @manager_view.displayAddView()

    handleRemovePayment: (id) ->
      card_model = @cards_collection.get id
      @removePayment card_model

    handleSelectPayment: (id) ->
      card_model = @cards_collection.get id
      @selectPayment card_model

    handleCancelPayment: ->
      @manager_view.displayShowView()

    handleSubmitPayment: ($form) ->
      StripeService.createToken $form

    handleStripeAuthorization: (response) ->
      card_json  = @card_model.toJSON()
      card_model = @sandbox.util.extend card_json, response.card, token: response.id
      @addPayment card_model


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @manager_view = new @views.manager
        model     : @card_model
        collection: @cards_collection

        subviews:
          add : @views.add
          show: @views.show

      @manager_view.render().$el

    onDestroy: ->
      @manager_view.$el.remove()



  # exports
  PaymentController
