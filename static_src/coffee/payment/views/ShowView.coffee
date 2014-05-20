define [
  'BaseView'
],
(BaseView) ->


  class ShowView extends BaseView

    initialize: (settings={}) ->
      #

    render: ->
      @$el.html '<h1>ShowView</h1>'
      @


    ###*
     * Event Handlers
    ###



  # exports
  ShowView
