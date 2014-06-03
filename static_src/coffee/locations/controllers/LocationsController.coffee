define [
  'BaseController'
],
(BaseController) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      @locations_collection = new @collections.locations()

      # fetch the collection
      @sandbox.on 'resource:uri', @handleUpdatingCollectionUri, @
      @sandbox.on 'location:selected', @handleLocationSelection, @


    ###*
     * Event Handlers
    ###
    handleUpdatingCollectionUri: (resource_uri) ->
      @locations_collection.url = resource_uri
      @locations_collection.fetch()


    handleLocationSelection: (location_id) ->
      model = @locations_collection.findWhere id: location_id
      meals_uri = model.get 'meals_uri'

      if meals_uri?
        @sandbox.publish 'meals:resource:uri', meals_uri


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
