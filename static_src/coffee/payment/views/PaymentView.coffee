define [
  'facade'
  'BaseView'
],
(facade, BaseView) ->


  class PaymentView extends BaseView

    initialize: (settings={}) ->
      # install sandbox to view
      @sandbox ?= facade.installTo {}, 'payment'

      # set values
      @sandbox.value greeting: 'Allo'

      # initial welcome
      @sandbox.on      'welcome', @handleWelcome, @
      @sandbox.trigger 'welcome', 'PaymentView'


    render: ->
      @$el.html '<h1>PaymentView</h1>'
      @


    ###*
     * Event Handlers
    ###
    handleWelcome: ->
      greeting = @sandbox.value().greeting
      console?.log "#{greeting}, PaymentView, and welcome!!"


  # exports
  PaymentView
