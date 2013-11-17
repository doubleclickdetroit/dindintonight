# imports
# Backbone.View



class MealView extends Backbone.View

  tagName  : 'section'
  className: 'food_module meat'

  events: {
    'click .counter_plus'     : 'handleIncrement'
    'click .counter_minus'    : 'handleDecrement'
    'keyup .quantity_food_1' : 'handleManualQuantity'
  }

  initialize: (settings) ->
    super

    # cache template
    @tmpl = settings.tmpl

    # listen to model
    @model.on 'change:quantity', @fillInQuantity, @


  render: ->
    @$el.html @tmpl @model.attributes
    @


  fillInQuantity: ->
    @$( '.quantity_food_1').val @model.get( 'quantity' )


  ### Event Handlers ###
  handleIncrement: (evt) ->
    evt.preventDefault()
    qty = @model.get 'quantity'
    @model.set quantity: ++qty


  handleDecrement: (evt) ->
    evt.preventDefault()
    qty = @model.get 'quantity'
    @model.set( quantity: --qty ) if qty > 0


  handleManualQuantity: (evt) ->
    qty = $( evt.currentTarget ).val()
    # console.log qty, @model.get( 'quantity' ), $.isNumeric qty
    if $.isNumeric qty
      @model.set { quantity: qty }, { silent: true }
    else
      @fillInQuantity()




# exports
window.dd.Views.MealView = MealView