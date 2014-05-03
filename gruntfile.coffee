# app config
dindin_config =
  app    : './'
  src    : 'static_src'
  release: 'static'
  components:
    all      : 'lib'
    managed  : 'lib/bower_components'
    unmanaged: 'lib/other_components'
  build: require './buildfile'

# grunt scope
gruntFn = (grunt) ->

  # load all grunt tasks
  require( 'load-grunt-tasks' ) grunt

  # configuration
  gruntConfig =

    app_config: dindin_config

    clean:
      tmp     : '<%= app_config.src %>/.tmp'
      release : '<%= app_config.release %>'

    coffee:
      release:
        files: [{
          expand: true
          cwd: '<%= app_config.src %>/coffee'
          src: '**/*.coffee'
          dest: '<%= app_config.src %>/.tmp/js'
          ext: '.js'
        }]

      dev:
        files: [{
          expand: true
          cwd: '<%= app_config.src %>/coffee'
          src: '**/*.coffee'
          dest: '<%= app_config.release %>/js'
          ext: '.js'
        }]

      test:
        files: [{
          expand: true
          cwd: '<%= app_config.src %>/test/spec'
          src: '**/*.coffee'
          dest: '<%= app_config.release %>/test/spec'
          ext: '.js'
        }]

    concurrent:
      dev:
        tasks : [
          'watch'
        ]
        options :
          logConcurrentOutput : true

    sass:
      release:
        files: [{
          expand: true
          cwd: '<%= app_config.src %>/scss/'
          src: '**/*.scss'
          dest: '<%= app_config.src %>/.tmp/css'
          ext: '.css'
        }]

      dev:
        files: [{
          expand: true
          cwd: '<%= app_config.src %>/scss/'
          src: '**/*.scss'
          dest: '<%= app_config.release %>/css'
          ext: '.css'
        }]

      options:
        style: '  compressed'
        loadPath: [
          '<%= app_config.src %>/scss'
          '<%= app_config.src %>/<%= app_config.components.managed %>'
          '<%= app_config.src %>/<%= app_config.components.unmanaged %>'
        ]

    copy:
      lib:
        files:[
          dot    : true
          expand : true
          cwd    : '<%= app_config.src %>'
          dest: '<%= app_config.release %>'
          src: '<%= app_config.components.all %>/**/*.js'
        ]
      fonts:
        files:[
          cwd    : '<%= app_config.src %>/<%= app_config.components.managed %>/Font-Awesome'
          expand : true
          dest: '<%= app_config.release %>'
          src: 'fonts/**'
        ]
      images:
        files: [
          dot    : true
          expand : true
          cwd    : '<%= app_config.src %>'
          dest: '<%= app_config.release %>'
          src: 'images/**/*'
        ]

      tmp_css:
        files:[
          dot    : true
          expand : true
          cwd    : '<%= app_config.src %>'
          dest: '<%= app_config.release %>'
          src: '.tmp/**/*.css'
        ]
      tmp_js:
        files:[
          dot    : true
          expand : true
          cwd    : '<%= app_config.src %>'
          dest: '<%= app_config.release %>'
          src: '.tmp/**/*.js'
        ]
    jasmine:
      all:
        src: '<% app_config.release %>/js/**/*.js'
        options:
          keepRunner: true
          specs : '<%= app_config.release %>/test/spec/{,*/}*.js'
          template: require( 'grunt-template-jasmine-requirejs' )
          templateOptions:
            requireConfigFile: './static/js/main.js'
            requireConfig:
              baseUrl: 'static/js'

    requirejs:
      compile:
        options: dindin_config.build

    watch:
      html:
        files: ['**/templates/*.html']
        options:
          livereload: true

      css:
        files: ['<%= app_config.src %>/scss/**/*.scss']
        tasks: ['sass:dev']
        options:
          livereload: true
          # Required to avoid 'build' being run twice
          spawn: false

      js:
        files: ['<%= app_config.src %>/coffee/**/*.coffee']
        tasks: ['coffee:dev']
        options:
          livereload: true
          # Required to avoid 'build' being run twice
          spawn: false

      images:
        files:['<%= app_config.src %>/images/**/*']
        tasks: ['copy:images']
        options:
          livereload: true

      test:
        files: ['<%= app_config.src %>/**/*.coffee']
        tasks: ['build:test','jasmine']

  # register tasks

  # By default, run a build, start the webserver, and watch for changes
  grunt.registerTask 'copy:release', [
    'copy:lib'
    'copy:fonts'
    'copy:images'
    'copy:tmp_css'
    'copy:tmp_js'
  ]

  grunt.registerTask 'copy:dev', [
    'copy:lib'
    'copy:fonts'
    'copy:images'
  ]

  grunt.registerTask 'compile:release', [
    'coffee:release'
    'sass:release'
  ]

  grunt.registerTask 'compile:dev', [
    'coffee:dev'
    'sass:dev'
  ]

  grunt.registerTask 'compile:test', [
    'coffee:test'
  ]

  grunt.registerTask 'build:release', [
    'clean'
    'compile:release'
    'requirejs'
    'copy:release'
    'clean:tmp'
  ]

  grunt.registerTask 'build:dev', [
    'clean'
    'compile:dev'
    'copy:dev'
  ]

  grunt.registerTask 'build:test', [
    'compile:dev'
    'compile:test'
    'jasmine'
  ]

  grunt.registerTask 'test', [
    'copy:dev'
    'build:test'
    'watch:test'
  ]

  grunt.registerTask 'default', [
    'build:dev'
    'concurrent:dev'
  ]

  # init grunt with config
  grunt.initConfig gruntConfig


# export grunt
module.exports = gruntFn
