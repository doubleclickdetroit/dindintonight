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
    top = @$el.offset().top
    @$el.html @tmpl()
    setTimeout (-> $( 'body, html' ).animate scrollTop: top ), 1500


  ### Event Handlers ###
  handlePaymentEvent: (type, attrs) ->
    @render() if type is 'change'


  handleFieldChange: (evt) =>
    console.log 'handleFieldChange', evt.currentTarget



# exports
window.dd.Views.PaymentView = PaymentView