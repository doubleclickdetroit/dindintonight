define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class MapService extends BaseService

    constants: {}

    initialize: ->
      #


    ###
      # Event Handlers
    ###



  # Register service
  facade.register 'map', MapService