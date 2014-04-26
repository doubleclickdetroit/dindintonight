define [
  'core/mediator'
  'BaseModule'
  'BaseService'
],
(mediator, BaseModule, BaseService) ->


  describe 'testing the mediator', ->
    it 'should be defined', ->
      expect( mediator ).toBeDefined()


    describe 'utilities', ->

      describe 'camelize string', ->
        it 'should be defined', ->
          expect( mediator.util.camelize ).toBeDefined()

        it 'should came-case a snake-cased string', ->
          str = 'my_awesome_classname'
          result = mediator.util.camelize str

          expect( result ).toEqual 'MyAwesomeClassname'


      describe 'decamelize string', ->
        it 'should be defined', ->
          expect( mediator.util.decamelize ).toBeDefined()

        it 'should snake-case a camel-cased string', ->
          str = 'MyAwesomeClassname'
          result = mediator.util.decamelize str

          expect( result ).toEqual 'my_awesome_classname'


      describe 'constantize string', ->
        it 'should be defined', ->
          expect( mediator.util.constantize ).toBeDefined()

        it 'should constantize a camel-cased string', ->
          str = 'my_property_name'
          result  = mediator.util.constantize str

          expect( result ).toEqual 'MY_PROPERTY_NAME'


    describe 'modules', ->
      class Foo extends BaseModule
      class Bar extends BaseModule
      class Baz extends BaseService

      beforeEach ->
        mediator.register 'foo', Foo
        mediator.register 'bar', Bar
        mediator.register 'baz', Baz

      describe 'register module', ->
        it 'should be defined', ->
          expect( mediator.register ).toBeDefined()

        it 'should accept a channel and a module', ->
          spyOn mediator, 'register'

          channel = 'test'
          module  = BaseModule

          # register module
          mediator.register channel, module
          expect( mediator.register ).toHaveBeenCalledWith channel, module

        it 'should register a subclass of BaseService as an instance', ->
          channel = 'baz'
          module  = null

          # async test
          waitsFor ->
            mediator.require channel, (resource) ->
              module = resource
              true

          runs ->
            expect( module instanceof BaseService ).toBeTruthy()


      describe 'require module', ->
        it 'should be defined', ->
          expect( mediator.require ).toBeDefined()

        it 'should load a dependency as a string', ->
          dep = 'foo'
          module = null

          # async test
          waitsFor ->
            mediator.require dep, (resource) ->
              module = resource
              true

          runs ->
            expect( module.__super__.constructor is BaseModule ).toBeTruthy()

        it 'should load a dependencies as an array', ->
          deps = ['foo','bar','baz']
          modules = []

          # async test
          waitsFor ->
            mediator.require deps, (resource) ->
              modules.push resource
              true

          runs ->
            expect( modules.length ).toEqual deps.length

        it 'should broadcast a "loaded" event when required module has loaded', ->
          dep = 'foo'
          obj = handleLoadedEvent: ->

          # setup spy
          spyOn obj, 'handleLoadedEvent'

          # listen and then require
          mediator.subscribe dep+':loaded', obj.handleLoadedEvent
          mediator.require dep

          expect( obj.handleLoadedEvent ).toHaveBeenCalled()

        it 'should accept a callback that is called with the module as the argument', ->
          dep = 'foo'
          obj = handleCallback: ->

          # setup spy
          spyOn obj, 'handleCallback'

          # require module with callback
          mediator.require dep, obj.handleCallback

          expect( obj.handleCallback ).toHaveBeenCalledWith Foo