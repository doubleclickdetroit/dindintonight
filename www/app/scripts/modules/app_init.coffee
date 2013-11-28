define [ 'libs/mediator' ], (mediator) ->

  mediator.subscribe 'appInit', ->

    console.log 'appInit module', arguments