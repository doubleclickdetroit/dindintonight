define [
  'BaseView'
  'hbs!../templates/order'
  'hbs!../templates/summary'
],
(BaseView, hbs_order, hbs_summary) ->


  class OrderView extends BaseView

    events:
      'click #btn-order' : 'handleSubmitOrder'

    initialize: (settings={}) ->
      # initially render and inject the template
      @$el.html hbs_order( @serialize() )

      # cache elements
      @$summary = @$ '#summary'
      @$submit  = @$( '#btn-order' ).attr 'disabled', true

      # model listeners
      @model.on 'change', @render, @

    serialize: ->
      attrs = @model.toJSON()

      @sandbox.util.extend attrs, {
        has_orders : @model.hasOrders()
        total_price: @model.getTotalPrice()
      }

    render: ->
      # fill-in the summary
      @$summary.html hbs_summary( @serialize() )

      # fill-in the submit button
      @$submit.attr 'disabled', !@model.isValid()

      @


    ###*
     * Event Handlers
    ###
    handleSubmitOrder: (evt) ->
      json_string = JSON.stringify @model.attributes
      @sandbox.trigger 'submit'



  # exports
  OrderView
