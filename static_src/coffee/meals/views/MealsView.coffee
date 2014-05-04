define [
  'facade'
  'BaseView'
],
(facade, BaseView) ->


  class MealsView extends BaseView

    initialize: (settings={}) ->
      # install sandbox to view
      @sandbox ?= facade.installTo {}, 'meals'

      # set values
      @sandbox.value greeting: 'Allo'

      # initial welcome
      @sandbox.on      'welcome', @handleWelcome, @
      @sandbox.trigger 'welcome', 'MealsView'


    render: ->
      @$el.html '<h1>MealsView</h1>'
      @


    ###*
     * Event Handlers
    ###
    handleWelcome: ->
      greeting = @sandbox.value().greeting
      console?.log "#{greeting}, MealsView, and welcome!!"


  # exports
  MealsView
