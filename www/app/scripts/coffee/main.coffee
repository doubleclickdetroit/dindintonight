'use strict'



require.config

  shim:
    underscore:
      exports: '_'

    backbone:
      deps: [
        'underscore',
        'jquery'
      ]
      exports: 'Backbone'

    bootstrap:
      deps: [
        'jquery'
      ]
      exports: 'jquery'

    handlebars:
      exports: 'Handlebars'

  paths:
    # components
    text      : '../bower_components/requirejs-text/text'
    jquery    : '../bower_components/jquery/jquery'
    backbone  : '../bower_components/backbone/backbone'
    underscore: '../bower_components/underscore/underscore'
    bootstrap : 'vendor/bootstrap'
    handlebars: '../bower_components/handlebars/handlebars.amd'

    # directories
    tmpl: 'templates'



require ['backbone'], (Backbone) ->
  console.log 'Hello, World!'
  Backbone.history.start()