define [ 'jquery', 'underscore', 'backbone', 'core/mediator' ], ($, _, Backbone, mediator) ->


  mediator.dom  = $
  mediator.util = _
  mediator.mvc  = Backbone



  # exports
  mediator