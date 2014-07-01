define [
  'BaseView'
],
(BaseView) ->


  class ManagerView extends BaseView

    events: {}


    initialize: ->
      super

      # create subviews
      @add_view  = new @subviews.add  model: @model, collection: @collection
      @show_view = new @subviews.show model: @model, collection: @collection

      # initially inject subviews
      @$el.append @add_view.$el
      @$el.append @show_view.$el

      # collection listeners
      @collection.on 'reset add remove', @displayShowView, @


    render: ->
      # default display show view
      @displayShowView()
      @


    displayShowView: ->
      @add_view.hide()
      @show_view.render().show()


    displayAddView: ->
      @show_view.hide()
      @add_view.render().show()


    ###
      # Event Handlers
    ###



  # exports
  ManagerView