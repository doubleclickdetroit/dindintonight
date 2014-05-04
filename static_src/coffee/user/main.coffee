define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class UserService extends BaseService

    constants: {}

    initialize: ->
      #


    ###
      # Event Handlers
    ###



  # Register service
  facade.register 'user', UserService