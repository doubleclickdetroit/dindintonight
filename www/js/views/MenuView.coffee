# imports
BaseView = window.dd.Views.BaseView



class MenuView extends BaseView

  initialize: (settings) ->
    @events = settings.events



# exports
window.dd.Views.MenuView = MenuView