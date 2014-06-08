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
      @sandbox.on 'create', @handleAssigningCollectionUri, @


    ###*
     * Event Handlers
    ###
    handleAssigningCollectionUri: ->
      # handle assigning resource_uri to UserService
      # this is a bit unconventional as all other resources
      # are handled internally by UserService
      resource_uri = @bootstrap.resource_uri
      UserService.assignLocationResourceUri resource_uri


    ###*
     * Create & Destroy Methods
    ###
    onCreate: ->
      @locations_view = new @views.locations
        collection: @locations_collection
        subviews:
          location: @views.location

      @locations_view.$el

    onDestroy: ->
      @locations_view.$el.remove()



  # exports
  LocationsController
