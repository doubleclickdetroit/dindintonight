define [
  'BaseView'
  'hbs!../templates/show'
],
(BaseView, hbs_show) ->


  class ShowView extends BaseView

    events:
      'click .btn-add'  : 'handleAddButton'
      'click .btn-edit' : 'handleEditButton'


    initialize: (settings={}) ->
      super

    serialize: ->
      @collection.toJSON()

    render: ->
      cards_serialized = cards: @serialize()
      @$el.html hbs_show( cards_serialized )
      @


    ###*
     * Event Handlers
    ###
    handleAddButton: (evt) ->
      evt.preventDefault()
      @sandbox.trigger 'payment:add'

    handleEditButton: (evt) ->
      evt.preventDefault()
      card_id = @sandbox.dom.find( evt.target ).data 'card-id'
      @sandbox.trigger 'payment:edit', card_id



  # exports
  ShowView
