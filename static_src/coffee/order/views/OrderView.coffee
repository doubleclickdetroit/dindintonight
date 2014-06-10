define [
  'BaseView'
  'hbs!../templates/order'
],
(BaseView, hbs_order) ->


  class OrderView extends BaseView

    initialize: (settings={}) ->
      # initially render and inject the template
      @$el.html hbs_order( @serialize() )


    render: ->
      @


    ###*
     * Event Handlers
    ###



  # exports
  OrderView
