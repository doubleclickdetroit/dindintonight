define [
  'BaseView'
  'hbs!../templates/meals'
],
(BaseView, hbs_meals) ->


  class MealsView extends BaseView

    initialize: (settings={}) ->
      super

      # initially inject the collection template
      @$el.html hbs_meals( title: 'MealsView' )

      # cache elements
      @$meals = @$ '.meals'

      # collection listeners
      @collection.on 'sync', @render, @


    render: ->
      @collection.each (meal_model) =>
        meal_view = new @subviews.meal model: meal_model
        @$meals.append meal_view.$el

      @


    ###*
     * Event Handlers
    ###


  # exports
  MealsView
