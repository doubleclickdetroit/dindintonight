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
      @user_model = new UserModel module.config()


    is_loggedin: ->
      @user_model.is_loggedin()



  # Register service
  facade.register 'user', UserService