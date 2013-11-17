# imports
Views       = window.dd.Views
Models      = window.dd.Models
Collecitons = window.dd.Collecitons



class ApplicationController

  constructor: (settings) ->
    @events = settings.events

    @events.on 'payment-module', (state) ->
      console.log "ApplicationController 'payment-module #{state}'"



# exports
window.dd.Controllers.ApplicationController = ApplicationController