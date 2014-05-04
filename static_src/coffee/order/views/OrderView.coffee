define [
  'BaseView'
  'text!../templates/order.html'
],
(BaseView, tmpl_order) ->


  class OrderView extends BaseView

    initialize: (settings={}) ->
      #


    render: ->
      @$el.html tmpl_order
      @


    ###*
     * Event Handlers
    ###



  # exports
  OrderView
