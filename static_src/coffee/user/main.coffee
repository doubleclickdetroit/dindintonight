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


    ###
      # Private Methods
    ###
    getBootstrapData = ->
      facade.util.extend module.config(), {
        # mock data
        cards: [
          {
            id: 1234567890
            name_first: 'Ben'
            name_last: 'Babics'
            brand: 'Discover'
            last4: '1234'
            exp_month: '05'
            exp_year : '2017'
          }
        ]
      }



  # Register service
  facade.register 'user', UserService