define [
  'facade'
  'BaseView'
],
(facade, BaseView) ->


  class OrderView extends BaseView

    initialize: (settings={}) ->
      # install sandbox to view
      @sandbox ?= facade.installTo {}, 'order'

      # set values
      @sandbox.value greeting: 'Allo'

      # initial welcome
      @sandbox.on      'welcome', @handleWelcome, @
      @sandbox.trigger 'welcome', 'OrderView'


    render: ->
      @$el.html '<h1>OrderView</h1>'
      @


    ###*
     * Event Handlers
    ###
    handleWelcome: ->
      greeting = @sandbox.value().greeting
      console?.log "#{greeting}, OrderView, and welcome!!"


  # exports
  OrderView
