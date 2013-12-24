define [ './mediator' ], (mediator) ->


  subscribe: (args...) ->
    mediator.subscribe args...

  publish: (args...) ->
    mediator.publish args...