# imports
BaseView = window.dd.Views.BaseView



class MealsView extends BaseView

  initialize: (settings) ->
    super

    # listeners
    @events.on 'meals', @handleMealsUpdate, @

    # cache elements
    @$container = @$ '#view-meal'


  render: (meals) ->
    meals.each (meal) => @$container.append @tmpl( meal.attributes )


  ### Event Handlers ###
  handleMealsUpdate: (evt, meals) ->
    @render( meals ) if evt is 'reset'



# exports
window.dd.Views.MealsView = MealsView