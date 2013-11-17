# imports
BaseView = window.dd.Views.BaseView



class LocationView extends BaseView

  initialize: ->
    super

    # temp hard-code rendering & parsing of tmpl
    @render()


  render: ->
    @$el.html @tmpl()



# exports
window.dd.Views.LocationView = LocationView