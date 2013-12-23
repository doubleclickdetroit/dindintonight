define [ 'core/facade', './mediator' ], (facade, mediator) ->


  facade.mvc = mediator.mvc
  facade.dom = mediator.dom



  # exports
  facade