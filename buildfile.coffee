module.exports =

  appDir : 'static_src/.tmp/'

  baseUrl: 'js/'

  mainConfigFile: 'static_src/.tmp/js/main.js'

  dir: 'static'

  paths:
    # Libs
    jquery       : '../../lib/bower_components/jquery/jquery'
    underscore   : '../../lib/bower_components/underscore/underscore'
    backbone     : '../../lib/bower_components/backbone/backbone'
    bootstrap    : '../../lib/bower_components/sass-bootstrap/dist/js/bootstrap'
    fb           : '//connect.facebook.net/en_US/all'
    localstorage : '../../lib/bower_components/backbone.localStorage/backbone.localStorage-min'
    text         : '../../lib/bower_components/requirejs-text/text'
    plate        : '../../lib/other_components/plate/dist/plate'
    jinja        : '../../lib/other_components/jinja.js/lib/jinja'
    # Core
    facade          : 'core/facade'
    BaseView        : 'core/views/BaseView'
    BaseModule      : 'core/modules/BaseModule'
    BaseService     : 'core/services/BaseService'
    BaseController  : 'core/controllers/BaseController'
    # Aliases
    helpers : 'core/helpers/'
    django  : '../../../'


  modules: [
    {
      name   : 'main'
      include: ['backbone','bootstrap','BaseModule','BaseService','BaseController','BaseView']
    }
    # !! Generator Adds Module Here !!
  ]
