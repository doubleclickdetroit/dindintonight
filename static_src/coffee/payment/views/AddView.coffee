define [
  'BaseView'
  'hbs!../templates/add'
],
(BaseView, tmpl_edit) ->


  class AddView extends BaseView

    events:
      'submit'            : 'handleFormSubmission'
      'click .btn-cancel' : 'handleCancelSubmission'
      'change [data-stripe^="name"]'   : 'updateAttribute'
      'change [data-stripe^="address"]': 'updateAttribute'


    initialize: (settings={}) ->
      super

    render: ->
      @$el.html tmpl_edit( @serialize() )
      @

    updateAttribute: (evt) ->
      $field = @sandbox.dom.find evt.target
      name   = $field.attr 'data-stripe'
      val    = $field.val() || null

      # update the model
      @model.set name, val


    ###*
     * Event Handlers
    ###
    handleFormSubmission: (evt) ->
      evt.preventDefault()
      return unless @model.isValid()
      @sandbox.trigger 'payment:submit', @$( '#payment-form' )

    handleCancelSubmission: (evt) ->
      evt.preventDefault()
      @sandbox.trigger 'payment:cancel'



  # exports
  AddView
