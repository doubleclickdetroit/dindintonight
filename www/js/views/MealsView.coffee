# imports
BaseView = window.dd.Views.BaseView



class MealsView extends BaseView

  initialize: (settings) ->
    @events = settings.events

    # cache template
    @tmpl = settings.template

    # listeners
    @on 'meals', 'reset', @render, @


  render: ->
    console.log 'MealsView render', arguments



# exports
window.dd.Views.MealsView = MealsView