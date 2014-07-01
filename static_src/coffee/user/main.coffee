define [
  'module'
  'facade'
  'BaseService'
  'user/models/UserModel'
],
(module, facade, BaseService, UserModel) ->


  class UserService extends BaseService

    constants: {}

    initialize: ->
      bootstrap_data = getBootstrapData()
      @user_model = new UserModel bootstrap_data


    ###
      # Public Methods
    ###
    isLoggedIn: ->
      @user_model.isLoggedIn()

    getCards: ->
      @user_model.get 'cards'

    getUser: ->
      @user_model.toJSON()


    ###
      # Private Methods
    ###
    getBootstrapData = ->
      facade.util.extend module.config()



  # Register service
  facade.register 'user', UserService