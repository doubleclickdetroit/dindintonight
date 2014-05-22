define [
  'facade'
  'BaseService'
],
(facade, BaseService) ->


  class MapService extends BaseService

    $api = null

    constants:
      API_FN : 'mapsApiInitialize'
      API_KEY: 'AIzaSyC-rbtKvoVTkbBME7aIAvBs2f-S917uXcg'


    initialize: ->
      loadScript.apply @


    loadScript = ->
      api_fn = @constant().API_FN

      script = document.createElement('script')
      script.type = 'text/javascript'
      script.src = "https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&callback=#{api_fn}"
      document.body.appendChild(script)

      window[api_fn] = =>
        if $api?
          console?.log 'MapService API has already been initialized.'
        else
          handleMapsApiInitialize.apply @


    ###
      # Event Handlers
    ###
    handleMapsApiInitialize = ->
      $api = google.maps
      @trigger 'ready'



  # Register service
  facade.register 'map', MapService