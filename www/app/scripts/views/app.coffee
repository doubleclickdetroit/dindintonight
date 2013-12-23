define [ 'extensions/facade' ], (facade) ->


  class AppView extends facade.mvc.baseView

    initialize: ->
      #
      console.log 'AppView initialized', @



  # exports
  AppView