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

      title: data.client.name

      location:
        lat: data.location.latitude
        lng: data.location.longitude

      image:
        url: data.images[0].location



  # exports
  LocationModel