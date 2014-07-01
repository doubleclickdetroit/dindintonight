define [
  'BaseModel'
],
(BaseModel) ->


  class UserModel extends BaseModel

    urlRoot: ->
      @get 'resource_uri'

    defaults:
      email          : ''
      username       : ''
      first_name     : ''
      last_name      : ''
      cards          : []
      locations      : []
      social_accounts: []


    isLoggedIn: ->
      @get( 'id' )?

    toJSON: ->
      @omit 'cards', 'locations'



  # exports
  UserModel