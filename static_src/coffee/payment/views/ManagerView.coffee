define [
  'BaseView'
  './EditView'
  './ShowView'
],
(BaseView, EditView, ShowView) ->


  class ManagerView extends BaseView

    events: {}


    initialize: (settings={}) ->
      #


    render: ->
      @$el.html '<h1>ManagerView</h1>'
      @


    ###
      # Event Handlers
    ###



  # exports
  ManagerView