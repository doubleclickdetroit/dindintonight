define [
  '../views/PaymentView'
  '../views/ManageView'
],
(PaymentView, ManageView) ->


  ViewFactory = (view_id) ->

    switch view_id
      when 'manage' then ManageView
      else               PaymentView



  # exports
  ViewFactory