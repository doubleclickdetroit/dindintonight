# imports
Models   = window.dd.Models
BaseView = window.dd.Views.BaseView



class LocationView extends BaseView

  events: {
    'click #btn-location' : 'handleLocationLookup'
  }

  initialize: ->
    super

    # define view model
    @model = new Models.LocationModel()

    # cache elements
    @map           = null
    @marker        = null
    @$txt_location = @$ '#physical_location'
    @canvas_map    = @$( '#geo_map' ).get 0
    @geocoder      = new google.maps.Geocoder()

    # dom listeners
    $( '#btn-location' ).click @handleLocationLookup

    # listeners
    @model.on 'change:latlng', @render, @

    # initially setup map
    @setupMap()


  setupMap: ->
    latlng = new google.maps.LatLng 42.33556, -83.04926999999998

    mapOptions =
      zoom     : 16
      center   : latlng
      disableDefaultUI: true
      mapTypeId: google.maps.MapTypeId.ROADMAP

    @map = new google.maps.Map @canvas_map, mapOptions


  render: ->
    # get the location
    location = @model.get 'latlng'

    # clear the marker if it exists
    @marker.setMap( null ) if @marker

    @events.trigger 'app', 'success', 'We found ya! Let\'s eat some DinDin.', 'Checkout now.'

    # center the map and place the marker
    @map.setCenter location
    @marker = new google.maps.Marker map:@map, position:location

    @events.trigger 'location', 'change'


  ### Event Handerls ###
  handleLocationLookup: =>
    address = @$txt_location.val()


    @geocoder.geocode {'address': address}, (results, status) =>
      if status is google.maps.GeocoderStatus.OK
        @model.set latlng: results[0].geometry.location

      else
        @events.trigger 'app', 'error', 'Uh Oh! We\'re armed with the power of Google Maps. Try a real address there next time, Buckaroo.'




# exports
window.dd.Views.LocationView = LocationView