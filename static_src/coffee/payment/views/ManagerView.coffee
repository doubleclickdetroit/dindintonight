define [
  'BaseView'
],
(BaseView) ->


  class ManagerView extends BaseView

    events: {}


    initialize: ->
      super

      # create subviews
      @edit_view = new @subviews.edit model: @model, collection: @collection
      @show_view = new @subviews.show model: @model, collection: @collection

      # initially inject subviews
      @$el.append @edit_view.$el
      @$el.append @show_view.$el

      # collection listeners
      @collection.on 'reset add remove', @displayShowView, @


    render: ->
      # default display show view
      @displayShowView()
      @


    displayShowView: ->
      @edit_view.hide()
      @show_view.render().show()


    displayEditView: (card_model) ->
      @model.reset card_model?.toJSON()
      @show_view.hide()
      @edit_view.render().show()


    ###
      # Event Handlers
    ###



  # exports
  ManagerView