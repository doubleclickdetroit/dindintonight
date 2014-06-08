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


    addAll: ->
      fragment = document.createDocumentFragment()

      @collection.each (meal_model) =>
        meal_view = @addOne meal_model
        fragment.appendChild meal_view.render().el

      fragment


    addOne: (meal_model) ->
      new @subviews.meal { model: meal_model }


    emptyResults: ->
      # this can be a template based on conditions passed in
      '<div class="alert alert-danger"><strong>Oh snap...</strong> Looks like there aren\'t any available meals at this time.</div>'


    render: ->
      # render meals or empty results
      $fragment = if @collection.length then @addAll() else @emptyResults()

      # populate the meals
      @$meals.html $fragment

      @


    ###*
     * Event Handlers
    ###


  # exports
  MealsView
