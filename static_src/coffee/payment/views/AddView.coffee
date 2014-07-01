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

      # sandbox listener
      @sandbox.on 'validation:error', @render, @

    render: (validation_error) ->
      serialized_json = @serialize()

      # add validation errors
      if validation_error?
        @sandbox.util.extend serialized_json, error: validation_error

      @$el.html tmpl_edit( serialized_json )
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
