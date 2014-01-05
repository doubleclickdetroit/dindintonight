define [ 'core/facade', 'extensions/mediator' ], (facade, mediator) ->


  facade.dom  = mediator.dom
  facade.util = mediator.util
  facade.mvc  = mediator.mvc



  # exports
  facade