define [
  'BaseView'
  'text!../templates/form.html'
],
(BaseView, tmpl_form) ->


  class ManageView extends BaseView

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
      @sandbox.trigger 'manage:submit', $form



  # exports
  ManageView
