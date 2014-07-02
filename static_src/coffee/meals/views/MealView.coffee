define [
  'BaseView'
  'hbs!../templates/meal'
],
(BaseView, hbs_meal) ->


  class MealView extends BaseView

    events:
      'click .add'    : 'handleAddQty'
      'click .remove' : 'handleRemoveQty'


    initialize: (settings={}) ->
      super

      # initially inject the template
      @$el.html hbs_meal( @serialize() )

      # cache elements
      @$output = @$ '.qty'

      # model listeners
      @model.on 'change', @render, @

    serialize: ->
      attrs  = @model.pick 'id', 'description', 'price', 'qty'
      images = @model.get 'images'

      @sandbox.util.extend attrs, {
        image_url: images[0].location
      }

    render: ->
      @$output.text @model.get('qty')
      @


    ###*
     * Event Handlers
    ###
    handleAddQty: (evt) ->
      @model.addQty()

    handleRemoveQty: (evt) ->
      @model.removeQty()


  # exports
  MealView
