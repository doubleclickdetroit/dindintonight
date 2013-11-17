# imports
BaseView = window.dd.Views.BaseView



class MealsView extends BaseView

  initialize: (settings) ->
    @events = settings.events



# exports
window.dd.Views.MealsView = MealsView