define [
  'BaseView'
  'hbs!../templates/locations'
],
(BaseView, hbs_locations) ->


  class LocationsView extends BaseView

    initialize: (settings={}) ->
      super

      # initially inject the template
      @$el.html hbs_locations( title: 'LocationsView' )

      # cache elements
      @$locations = @$ '#locations-list'

      # collection listeners
      @collection.on 'sync', @render, @


    addAll: ->
      fragment = document.createDocumentFragment()

      @collection.each (location_model) =>
        location_view = @addOne location_model
        fragment.appendChild location_view.render().el

      fragment


    addOne: (location_model) ->
      new @subviews.location { model: location_model }


    render: ->
      # populate the list of locations
      @$locations.html @addAll()

      @


    ###
      # Event Handlers
    ###



  # exports
  LocationsView
