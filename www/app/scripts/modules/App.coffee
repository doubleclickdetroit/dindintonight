define [ 'facade', 'views/App', 'backbone' ], (facade, AppView, Backbone) ->


  class AppModule

    constructor: ->
      appView = new AppView
        el: facade.dom 'body'



  facade.subscribe 'app-init', (args...) ->
    appModule = new AppModule args...