define [ 'jquery', 'underscore', 'core/mediator', 'backbone', 'views/AbstractView' ], ($, _, mediator, Backbone, AbstractView) ->


  mediator.dom  = $
  mediator.util = _



  # exports
  mediator