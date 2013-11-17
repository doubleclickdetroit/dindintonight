# imports
BaseView = window.dd.Views.BaseView



class PaymentView extends BaseView

  initialize: (settings) ->
    @events = settings.events



# exports
window.dd.Views.PaymentView = PaymentView