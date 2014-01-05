define (require) ->


  # load facade
  facade = require 'facade'

  # define modules
  Modules = [
    require './App'
    require './Navigation'
    require './Locations'
    require './Meals'
    require './Billing'
  ]


  facade.subscribe 'app-init', ->
    new Module() for Module in Modules