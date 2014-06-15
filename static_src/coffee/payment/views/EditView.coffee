define [
  'BaseView'
  'hbs!../templates/edit'
],
(BaseView, tmpl_edit) ->


  class EditView extends BaseView

    events:
      'submit'            : 'handleFormSubmission'
      'click .btn-cancel' : 'handleCancelSubmission'


    initialize: (settings={}) ->
      super


    render: (card_model={}) ->
      @$el.html tmpl_edit( card_model )
      @


    ###*
     * Event Handlers
    ###
    handleFormSubmission: (evt) ->
      evt.preventDefault()
      $form = @$ '#payment-form'
      @sandbox.trigger 'payment:submit', $form

    handleCancelSubmission: (evt) ->
      evt.preventDefault()
      @sandbox.trigger 'payment:cancel'



  # exports
  EditView
