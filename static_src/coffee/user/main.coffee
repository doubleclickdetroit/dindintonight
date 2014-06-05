define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class UserService extends BaseService

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

    registerPaymentResource: (payment_resource) ->
      unregisterResource @payment_resource
      @payment_resource = payment_resource
      registerResource @payment_resource, @delegatePaymentEvents, @


    ###
      # Resource URI Assignment
    ###
    assignLocationResourceUri: (resource_uri) ->
      @locations_resource.url = resource_uri
      @locations_resource.fetch() if resource_uri?

    assignMealsResourceUri: (resource_uri) ->
      @meals_resource.url = resource_uri
      @meals_resource.fetch() if resource_uri?

    assignPaymentResourceUri: (resource_uri) ->
      @payment_resource.url = resource_uri
      @payment_resource.fetch() if resource_uri?


    ###
      # Event Delegates
    ###
    delegateLocationsEvents: (evt, context, value, options) ->
      switch evt
        when 'change:selected' then @handleLocationSelected(context)

    delegateMealsEvents: (evt, context, value, options) ->
      console.log 'delegateMealsEvents', arguments

    delegatePaymentEvents: (evt, context, value, options) ->
      console.log 'delegatePaymentEvents', arguments


    ###
      # Event Handlers
    ###
    handleLocationSelected: (location_model) ->
      meals_uri = location_model.get 'meals_uri'
      @assignMealsResourceUri meals_uri


    ###
      # Private Methods
    ###
    unregisterResource = (resource) ->
      resource.off() if resource?.off?

    registerResource = (resource, handler_fn, context) ->
      resource.on 'all', handler_fn, context



  # Register service
  facade.register 'user', UserService