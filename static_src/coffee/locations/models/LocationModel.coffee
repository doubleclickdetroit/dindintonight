define [
  'BaseModel'
],
(BaseModel) ->


  class LocationModel extends BaseModel


    url: ->
      attrs = @attributes.resource_uri


    toJSON: ->
      data = @attributes

      title: data.client.name

      location:
        lat: data.location.latitude
        lng: data.location.longitude

      image:
        url: 'http://placehold.it/40x40'



  # exports
  LocationModel