define [
  'BaseController'
],
(BaseController) ->


  class LocationsController extends BaseController


    initialize: (settings) ->
      @locations_collection = new @collections.locations()

      # fetch the collection
      @sandbox.on 'create', @handleCreateController, @


    ###*
     * Event Handlers
    ###
    handleCreateController: ->
      @locations_collection.fetch()


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
