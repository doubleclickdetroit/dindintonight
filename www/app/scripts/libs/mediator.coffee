define [ 'jquery', 'underscore' ], ($, _) ->

  channels = {} # loaded modules and their callbacks


  subscribe: (channel, callback, context) ->
    channels[channel] ?= []
    channels[channel].push callback
    @

  publish: (channel, args...) ->
    return @autoload.apply @, arguments if not channels[channel]?
    subscriber args... for subscriber in channels[channel]
    @

  autoload: (channel, args...) ->
    file = @util.decamelize channel

    require [ "modules/#{file}" ], (module) ->
      subscriber args... for subscriber in channels[channel]


  util:
    decamelize: (camelCase, delimiter = '_') ->
      camelCase.replace( /([A-Z])/g, "#{delimiter}$1" ).toLowerCase()

    camelize: (str) ->
      str.replace /(?:^|[\-_])(\w)/g, (delimiter, c) -> if c then c.toUpperCase() else ''

    method: (fn, context) ->
      $.proxy fn, context