define [
  'BaseView'
  'hbs!../templates/show'
],
(BaseView, hbs_show) ->


  class ShowView extends BaseView

    events:
      'click .btn-add'    : 'handleAddButton'
      'click .btn-remove' : 'handleRemoveButton'
      'click .btn-select' : 'handleSelectButton'


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

    handleRemoveButton: (evt) ->
      evt.preventDefault()
      card_id = @sandbox.dom.find( evt.target ).data 'card-id'
      @sandbox.trigger 'payment:remove', card_id

    handleSelectButton: (evt) ->
      evt.preventDefault()
      card_id = @sandbox.dom.find( evt.target ).data 'card-id'
      @sandbox.trigger 'payment:select', card_id



  # exports
  ShowView
