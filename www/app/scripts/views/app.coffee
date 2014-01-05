define [ 'facade', 'views/AbstractView', 'hbs!tmpl/app' ],
(facade, AbstractView, tmpl) ->


  class AppView extends AbstractView

    initialize: ->
      super

      # define template
      @template = tmpl

      # render view
      @render()



  # exports
  AppView