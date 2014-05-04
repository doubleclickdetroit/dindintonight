define [
  'BaseView'
],
(BaseView) ->


  class PaymentView extends BaseView

    initialize: (settings={}) ->
      #


    render: ->
      @$el.html '<h1>PaymentView</h1>'
      @


    ###*
     * Event Handlers
    ###



  # exports
  PaymentView
