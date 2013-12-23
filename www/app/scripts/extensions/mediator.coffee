define [ 'jquery', 'underscore', 'backbone', 'core/mediator' ], ($, _, Backbone, mediator) ->


  mediator.util = (args...) ->
    _ args...

  mediator.dom = (args...) ->
    $ args...

  mediator.mvc =
    baseView      : Backbone.View
    baseModel     : Backbone.Model
    baseCollection: Backbone.Collection



  # exports
  mediator