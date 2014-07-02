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
      @pick 'client', 'client_url', 'details', 'id', 'location', 'resource_uri'

    isSelected: ->
      @set 'selected', true




  # exports
  LocationModel