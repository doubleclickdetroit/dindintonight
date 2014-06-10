define [
  'BaseView'
],
(BaseView) ->


  class ManagerView extends BaseView

    events: {}


    initialize: (settings={}) ->
      #


    render: ->
      @$el.html '<h1>PaymentView</h1>'
      @


    ###
      # Event Handlers
    ###



  # exports
  ManagerView