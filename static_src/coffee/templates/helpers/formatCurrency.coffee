define [
  'hbs/handlebars'
],
(Handlebars) ->


  formatCurrency = (amt) ->
    "$#{amt.toFixed(2).replace /(\d)(?=(\d{3})+(?:\.\d+)?$)/g, '$1,'}"


  # register helper with Handlebars
  Handlebars.registerHelper 'formatCurrency', formatCurrency



  # exports
  formatCurrency