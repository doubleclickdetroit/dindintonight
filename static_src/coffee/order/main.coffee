define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class OrderService extends BaseService

    constants: {}

    initialize: ->
      #


    ###
      # Event Handlers
    ###



  # Register service
  facade.register 'order', OrderService