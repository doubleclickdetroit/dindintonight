define [
  'BaseModel'
],
(BaseModel) ->


  class UserModel extends BaseModel

    urlRoot: '/api/v1/users'

    defaults:
      locations      : []
      social_accounts: []



  # exports
  UserModel