define [
  'BaseController'
  'UserService'
],
(BaseController, UserService) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      @locations_collection = new @collections.locations()
      UserService.registerLocationsResource @locations_collection

      # fetch the collection
      @sandbox.on 'create',            @handleAssigningCollectionUri, @
      @sandbox.on 'location:selected', @handleLocationSelection,      @


    ###*
     * Event Handlers
    ###
    handleAssigningCollectionUri: ->
      # handle assigning resource_uri to UserService
      # this is a bit unconventional as all other resources
      # are handled internally by UserService
      resource_uri = @bootstrap.resource_uri
      UserService.assignLocationResourceUri resource_uri

    handleLocationSelection: (location_id) ->
      @locations_collection.selectLocation location_id


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @locations_view = new @views.locations
        collection: @locations_collection

      @locations_view.$el

    onDestroy: ->
      @locations_view.$el.remove()



  # exports
  LocationsController
