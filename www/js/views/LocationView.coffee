# imports
BaseView = window.dd.Views.BaseView



class LocationView extends BaseView

  initialize: ->
    super

    # cache elements
    @$canvas_map = @$ '#geo_map'
    console.log '@$canvas_map', @$canvas_map

    # initially setup map
    @setupMap()


  setupMap: (attrs) ->
    myLatlng = new google.maps.LatLng -25.363882, 131.044922

    mapOptions = {
      zoom     : 10
      center   : myLatlng
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    map = new google.maps.Map @$canvas_map.get(0), mapOptions

    marker = new google.maps.Marker
      map     : map,
      position: myLatlng



# exports
window.dd.Views.LocationView = LocationView