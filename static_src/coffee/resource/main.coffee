define [
  'facade'
  'BaseService'
  'UserService'
],
(facade, BaseService, UserService) ->


  class ResourceService extends BaseService

    constants: {}

    initialize: ->
      #


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
      # Resource URI Assignment
    ###
    assignLocationResourceUri: (resource_uri) ->
      @locations_resource.url = resource_uri
      @locations_resource.fetch() if resource_uri?

    assignMealsResourceUri: (resource_uri) ->
      @meals_resource.url = resource_uri
      @meals_resource.fetch() if resource_uri?

    assignOrderResourceUri: (resource_uri) ->
      @orer_resource.url = resource_uri
      @orer_resource.fetch() if resource_uri?

    assignPaymentResourceUri: (resource_uri) ->
      @payment_resource.url = resource_uri
      @payment_resource.fetch() if resource_uri?


    ###
      # Event Delegates
    ###
    delegateLocationsEvents: (evt, context, value, options) ->
      switch evt
        when 'change:selected' then @handleLocationSelected(context)
        # else console.log 'delegateLocationsEvents', arguments

    delegateMealsEvents: (evt, context, value, options) ->
      switch evt
        when 'sync', 'change:qty' then @handleMealQuantity(context, value)
        # else console.log 'delegateMealsEvents', arguments

    delegateOrderEvents: (evt, context, value, options) ->
      console.log 'delegateOrderEvents', arguments

    delegatePaymentEvents: (evt, context, value, options) ->
      switch evt
        when 'change:selected' then @handlePaymentSelected(context)
        # else console.log 'delegatePaymentEvents', arguments


    ###
      # Event Handlers
    ###
    handleLocationSelected: (location_model) ->
      meals_uri = location_model.get 'meals_uri'
      @assignMealsResourceUri meals_uri
      @order_resource.updateLocation location_model

    handleMealQuantity: (meal_model, qty) ->
      meals_collection = @meals_resource.toJSON()
      @order_resource.updateMeals meals_collection

    handlePaymentSelected: (card_model) ->
      @order_resource.updateCard card_model


    ###
      # Private Methods
    ###
    unregisterResource = (resource) ->
      resource.off() if resource?.off?

    registerResource = (resource, handler_fn, context) ->
      resource.on 'all', handler_fn, context



  # Register service
  facade.register 'resources', ResourceService