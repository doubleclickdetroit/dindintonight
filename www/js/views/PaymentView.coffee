# imports
BaseView = window.dd.Views.BaseView



class PaymentView extends BaseView

  initialize: ->
    super

    # listeners
    @events.on 'location', @handlePaymentEvent, @


  render: ->
    @$el.html @tmpl()


  ### Event Handlers ###
  handlePaymentEvent: (type, attrs) ->
    @render() if type is 'change'



# exports
window.dd.Views.PaymentView = PaymentView