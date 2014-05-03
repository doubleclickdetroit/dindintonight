define [
  'user/models/UserModel'
],
(UserModel) ->


  describe 'test the UserModel', ->
    user = null

    beforeEach ->
      user = new UserModel

    it 'should be defined', ->
      expect( UserModel ).toBeDefined()

    it 'should point toward the right URI', ->
      expect( user.url() ).toBe '/api/v1/users'