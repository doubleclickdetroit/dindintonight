# imports
BaseView = window.dd.Views.BaseView



class PaymentView extends BaseView

  initialize: ->
    super

    # listeners
    @events.on 'location', @handlePaymentEvent, @

    # element listeners
    @$el.on 'change', 'input', @handleFieldChange


  render: ->
    @$el.html @tmpl()


  ### Event Handlers ###
  handlePaymentEvent: (type, attrs) ->
    @render() if type is 'change'


  handleFieldChange: (evt) =>
    console.log 'handleFieldChange', evt.currentTarget



# exports
window.dd.Views.PaymentView = PaymentView