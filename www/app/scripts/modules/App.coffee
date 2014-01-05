define [ 'facade', 'views/App', 'backbone' ],
(facade, AppView, Backbone) ->


  class AppModule

    constructor: ->
      appView = new AppView
        el: facade.dom 'body'



  # exports
  AppModule