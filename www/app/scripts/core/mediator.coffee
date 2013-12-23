define (require) ->


  channels = {} # loaded modules and their callbacks


  subscribe: (channel, callback, context) ->
    channels[channel] ?= []
    channels[channel].push callback
    @

  publish: (channel, args...) ->
    return unless channels[channel]?
    subscriber args... for subscriber in channels[channel]
    @