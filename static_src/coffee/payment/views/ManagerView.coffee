define [
  'BaseView'
],
(BaseView) ->


  class ManagerView extends BaseView

    events: {}


    initialize: ->
      super

      # create subviews
      @edit_view = new @subviews.edit collection: @collection
      @show_view = new @subviews.show collection: @collection

      # inject subviews
      @$el.append @edit_view.$el
      @$el.append @show_view.$el


    render: ->
      # default display show view
      @displayShowView()

      @


    displayShowView: ->
      @edit_view.hide()
      @show_view.render().show()


    displayEditView: (card_model) ->
      @show_view.hide()
      @edit_view.render(card_model).show()


    ###
      # Event Handlers
    ###



  # exports
  ManagerView