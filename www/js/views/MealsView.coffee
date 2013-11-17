# imports
Views = window.dd.Views



class MealsView extends Views.BaseView

  initialize: (settings) ->
    super

    # listeners
    @events.on 'meals', @handleMealsUpdate, @

    # cache elements
    @$container = @$ '#view-meal'


  render: (meals) ->
    meals.each (meal) =>
      mealView = new Views.MealView model: meal, tmpl: @tmpl
      @$container.append mealView.render().el


  ### Event Handlers ###
  handleMealsUpdate: (evt, meals) ->
    @render( meals ) if evt is 'reset'



# exports
window.dd.Views.MealsView = MealsView