define [
  'facade'
  'BaseService'
  'UserService'
  'BaseModel'
],
(facade, BaseService, UserService, BaseModel) ->


  class ResourceService extends BaseService

    constants: {}

    initialize: ->
      @view_manager = new BaseModel
        location: true
        meals   : false
        payment : true
        order   : false


    ###
      # Resource Methods
    ###
    registerLocationsResource: (locations_resource) ->
      unregisterResource @locations_resource
      @locations_resource = locations_resource
      registerResource @locations_resource, @delegateLocationsEvents, @

    registerMealsResource: (meals_resource) ->
      unregisterResource @meals_resource
      @meals_resource = meals_resource
      registerResource @meals_resource, @delegateMealsEvents, @

    registerOrderResource: (order_resource) ->
      unregisterResource @order_resource
      @order_resource = order_resource
      registerResource @order_resource, @delegateOrderEvents, @

      # initially bootstrap user data
      @order_resource.updateUser UserService.getUser()

    registerPaymentResource: (payment_resource) ->
      unregisterResource @payment_resource
      @payment_resource = payment_resource
      registerResource @payment_resource, @delegatePaymentEvents, @

      # initially bootstrap data
      @payment_resource.reset UserService.getCards(), { parse: true }


    ###
      # Event Delegates
    ###
    delegateLocationsEvents: (evt, context, value, options) ->
      switch evt
        when 'change:selected' then @handleLocationSelected(context)

    delegateMealsEvents: (evt, context, value, options) ->
      switch evt
        when 'sync', 'change:qty' then @handleMealQuantity(context, value)

    delegateOrderEvents: (evt, context, value, options) ->
      # console.log 'delegateOrderEvents', JSON.stringify(context)

    delegatePaymentEvents: (evt, context, value, options) ->
      switch evt
        when 'change:selected' then @handlePaymentSelected(context)


    ###
      # Event Handlers
    ###
    handleLocationSelected: (location_model) ->
      # set meals_uri and fetch meals
      meals_uri = location_model.get 'meals_uri'
      @meals_resource.url = meals_uri
      @meals_resource.fetch() if meals_uri?

      # update order_resource with location_model JSON
      @order_resource.updateLocation location_model.toJSON()

      # set view_manager if resources are valid
      @view_manager.set 'meals', @order_resource.isLocationValid()

    handleMealQuantity: (meal_model, qty) ->
      meals_collection = @meals_resource.getOrderedMeals()

      # update order_resource with meals_collection (is JSON)
      @order_resource.updateMeals meals_collection

      # set view_manager if resources are valid
      @view_manager.set 'order', @order_resource.isMealsValid()

    handlePaymentSelected: (card_model) ->
      # update order_resource with card_model JSON
      @order_resource.updateCard card_model.toJSON()


    ###
      # Private Methods
    ###
    unregisterResource = (resource) ->
      resource.off() if resource?.off?

    registerResource = (resource, handler_fn, context) ->
      resource.on 'all', handler_fn, context



  # Register service
  facade.register 'resources', ResourceService