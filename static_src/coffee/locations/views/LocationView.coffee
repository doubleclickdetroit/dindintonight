define [
  'BaseView'
  'hbs!../templates/location'
],
(BaseView, hbs_location) ->


  class LocationView extends BaseView

    events:
      'click' : 'handleOnSelection'


    serialize: ->
      attrs = @model.pick 'client', 'images'

      title    : attrs.client.name
      image_url: attrs.images[0].location

    render: ->
      serialized_json = @serialize()
      @$el.html hbs_location( serialized_json )

      @


    ###*
     * Event Handlers
    ###
    handleOnSelection: (evt) ->
      @model.isSelected()



  # exports
  LocationView
