define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class UserService extends BaseService

    constants: {}

    initialize: ->
      #



  # Register service
  facade.register 'user', UserService