# imports
BaseView = window.dd.Views.BaseView



class LocationView extends BaseView

  initialize: (settings) ->
    @events = settings.events



# exports
window.dd.Views.LocationView = LocationView