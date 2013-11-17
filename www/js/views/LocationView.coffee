# imports
BaseView = window.dd.Views.BaseView



class LocationView extends BaseView

  initialize: ->
    super

    @setupMap()

    # temp hard-code rendering & parsing of tmpl
    @render()


  setupMap: ->
    el = $('<div>').get(0)

    mapOptions = {
      zoom     : 8
      mapTypeId: google.maps.MapTypeId.ROADMAP
      center   : new google.maps.LatLng -34.397, 150.644
    }

    map = new google.maps.Map el, mapOptions


  render: ->
    @$el.html @tmpl()



# exports
window.dd.Views.LocationView = LocationView