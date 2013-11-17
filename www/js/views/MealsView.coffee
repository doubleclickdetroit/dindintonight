# imports
BaseView = window.dd.Views.BaseView



class MealsView extends BaseView

  initialize: (settings) ->
    @events = settings.events

    # cache template
    @tmpl = settings.template

    console.log 'MealsView templates', @tmpl

    # listeners
    @on 'meals', 'reset', @render, @


  reset: ->
    console.log 'MealsView reset'



# exports
window.dd.Views.MealsView = MealsView