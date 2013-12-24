'use strict'


require.config

    shim:
        underscore:
            exports: '_'

        backbone:
            deps: [
                'underscore'
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
        # Directories
        tmpl: 'templates'

        # Helpers
        facade: 'extensions/facade'

        # Plugins
        text: '../bower_components/requirejs-text/text'
        hbs : '../bower_components/require-handlebars-plugin/hbs'

        # Libs
        bootstrap : 'vendor/bootstrap'
        jquery    : '../bower_components/jquery/jquery'
        backbone  : '../bower_components/backbone/backbone'
        underscore: '../bower_components/underscore/underscore'
        handlebars: '../bower_components/handlebars/handlebars'



require [ 'facade', 'modules/main' ], (facade) ->
    # init app
    facade.publish 'app-init'