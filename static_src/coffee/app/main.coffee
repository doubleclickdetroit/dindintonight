define [
  'facade'
  'BaseModule'
  './controllers/AppController'
],
(facade, BaseModule, AppController) ->


  class AppModule extends BaseModule

    controller: AppController

    initialize: ->
      # event listeners
      @on 'require', @handleLoadedSubModule, @


    createController: (Controller) ->
      # create the controller
      @controller = new Controller()


    ### Event Handlers ###
    handleLoadedSubModule: (module_name) ->
      @subscribe "#{module_name}:loaded", (Module) ->
        new Module().start()



  # register module
  facade.register 'app', AppModule
