define [
  'BaseView'
  'text!../templates/form.html'
],
(BaseView, tmpl_form) ->


  class EditView extends BaseView

    events:
      'submit' : 'handleFormSubmission'


    initialize: (settings={}) ->
      #


    render: ->
      @$el.html tmpl_form
      @


    ###*
     * Event Handlers
    ###
    handleFormSubmission: (evt) ->
      evt.preventDefault()
      $form = @$ '#payment-form'
      @sandbox.trigger 'payment:submit', $form



  # exports
  EditView
