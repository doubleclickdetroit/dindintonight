define [ 'backbone' ], (Backbone) ->


  class AbstractView extends Backbone.View

    initialize: (options={}) ->
      super

      # cache elements
      @subviews = []
      @template = @template ? null

      # have we included subviews?
      if options.subviews?.length
        @add subview for subview in options.subviews


    # helpers
    serialize: ->
      return @model.toJSON()      if @model?
      return @collection.toJSON() if @collection?
      {}


    # crud
    add: (subview) ->
      @trigger 'add-before'
      @subviews.push subview
      @$el.append subview.$el
      @trigger 'add-after'


    remove: ->
      @trigger 'remove-before'
      # remove subviews
      @remove @subviews[0] while @subviews.length
      # call super
      super
      @trigger 'remove-after'


    destroy: ->
      @trigger 'destroy-before'
      @remove()
      @unbind()
      @trigger 'destroy-after'


    # rendering
    show: ->
      @trigger 'show-before'
      @$el.show()
      @trigger 'show-after'


    hide: ->
      @trigger 'hide-before'
      @$el.hide()
      @trigger 'hide-after'


    render: (args...) ->
      @trigger 'render-before'

      # render the template, if one exists
      if @template?
        html = @template @serialize( args... )
        @$el.html html

      # notify subviews parent has rendered
      subview.trigger( 'render-parent', @$el ) for subview in @subviews

      @trigger 'render-after'

      @