define [
  'facade'
  'BaseView'
],
(facade, BaseView) ->


  class LocationsView extends BaseView

    initialize: (settings={}) ->
      # install sandbox to view
      @sandbox ?= facade.installTo {}, 'locations'

      # set values
      @sandbox.value greeting: 'Allo'

      # initial welcome
      @sandbox.on      'welcome', @handleWelcome, @
      @sandbox.trigger 'welcome', 'LocationsView'


    render: ->
      @$el.html '<h1>LocationsView</h1>'
      @


    ###*
     * Event Handlers
    ###
    handleWelcome: ->
      greeting = @sandbox.value().greeting
      console?.log "#{greeting}, LocationsView, and welcome!!"


  # exports
  LocationsView
