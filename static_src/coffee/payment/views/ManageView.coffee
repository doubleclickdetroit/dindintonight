define [
  'BaseView'
],
(BaseView) ->


  class ManageView extends BaseView

    initialize: (settings={}) ->
      #

    render: ->
      @$el.html '<h1>ManageView</h1>'
      @


    ###*
     * Event Handlers
    ###



  # exports
  ManageView
