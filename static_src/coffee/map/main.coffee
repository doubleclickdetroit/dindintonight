define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class MapService extends BaseService

    constants:
      API_KEY: 'AIzaSyC-rbtKvoVTkbBME7aIAvBs2f-S917uXcg'


    initialize: ->
      #


    ###
      # Event Handlers
    ###



  # Register service
  facade.register 'map', MapService