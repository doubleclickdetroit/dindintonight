define [
  'BaseView'
  'hbs!../templates/order'
  'hbs!../templates/summary'
],
(BaseView, hbs_order, hbs_summary) ->


  class OrderView extends BaseView

    initialize: (settings={}) ->
      # initially render and inject the template
      @$el.html hbs_order( @serialize() )

      # cache elements
      @$summary = @$ '#summary'

      # model listeners
      @model.on 'change', @render, @


    render: ->
      @$summary.html hbs_summary( @serialize() )
      @


    ###*
     * Event Handlers
    ###



  # exports
  OrderView
