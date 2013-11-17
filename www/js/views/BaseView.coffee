# imports
# Backbone.View



class BaseView extends Backbone.View

  initialize: (settings) ->
    # cache events
    @events = settings.events

    # cache template
    if settings.template
      @tmpl = Handlebars.compile settings.template.html()




# exports
window.dd.Views.BaseView = BaseView