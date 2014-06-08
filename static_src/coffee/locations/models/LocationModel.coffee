define [
  'BaseModel'
],
(BaseModel) ->


  class LocationModel extends BaseModel

    defaults:
      selected: false


    url: ->
      attrs = @attributes.resource_uri


    toJSON: ->
      data = @attributes

      title    : data.client.name
      image_url: data.images[0].location


    isSelected: ->
      @set 'selected', true




  # exports
  LocationModel