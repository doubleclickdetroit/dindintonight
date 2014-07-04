define [
  'backbone'
], (Backbone) ->


  class BaseView extends Backbone.View

    initialize: (settings={}) ->
      @subviews = settings.subviews if settings.subviews?

    serialize: ->
      # If a model exists
      return @model.toJSON() if @model?
      # If a collection exists
      return @collection.toJSON() if @collection?
      # Otherwise, here's nothing
      {}

    show: ->
      @$el.show()

    hide: ->
      @$el.hide()

    toggle: (is_visible) ->
      if is_visible then @show() else @hide()

    render: ->
      @serialize()
      @



  # exports
  BaseView