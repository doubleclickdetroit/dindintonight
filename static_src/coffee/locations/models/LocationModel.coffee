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

      id: data.id

      title: data.client.name

      lat: data.details.latitude
      lng: data.details.longitude

      serving_area:
        lat: data.location.latitude
        lng: data.location.longitude

      image:
        url: data.images[0].location




  # exports
  LocationModel