# imports
BaseModel = window.dd.Models.BaseModel



class LocationModel extends BaseModel

  initialize: ->

    # listeners
    @on 'change:latlng', @handleLatLngChange, @


  ### Event Handlers ###
  handleLatLngChange: ->
    @set isValid: _.isEmpty( @attributes )



# exports
window.dd.Models.LocationModel = LocationModel