define [ 'facade' ], (facade) ->


  class AbstractModule

    constructor: ->
      # install facade
      facade.installTo @

    initialize: ->
      # abstract method
      # subclasses can override



  # exports
  AbstractModule