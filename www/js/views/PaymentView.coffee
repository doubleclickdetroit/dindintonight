# imports
BaseView = window.dd.Views.BaseView



class PaymentView extends BaseView

  initialize: ->
    super

    # listeners
    @events.on 'location', @handlePaymentEvent, @
    @events.on 'totalprice', @fillinTotalPrice, @

    # element listeners
    @$el.on 'change', 'input', @handleFieldChange



  render: ->
    # render template
    @$el.html @tmpl { price: window.total_price } # sorry about this :'(

    # scroll top
    top = @$el.offset().top
    setTimeout (-> $( 'body, html' ).animate scrollTop: top ), 1500


  fillinTotalPrice: (total_price) ->
    @$( '#totalPrice' ).text total_price


  ### Event Handlers ###
  handlePaymentEvent: (type, attrs) ->
    @render() if type is 'change'


  handleFieldChange: (evt) =>
    val = $( evt.currentTarget ).val()




# exports
window.dd.Views.PaymentView = PaymentView