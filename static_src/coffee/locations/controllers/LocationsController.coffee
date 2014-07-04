define [
  'BaseController'
  'ResourceService'
],
(BaseController, ResourceService) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      @locations_collection = new @collections.locations()
      ResourceService.registerLocationsResource @locations_collection

      # fetch the collection
      @sandbox.on 'create', @handleAssigningCollectionUri, @


    ###*
     * Event Handlers
    ###
    handleAssigningCollectionUri: ->
      # handle assigning resource_uri to the locations_collection
      resource_uri = @bootstrap.resource_uri
      @locations_collection.url = resource_uri
      @locations_collection.fetch() if resource_uri?


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
