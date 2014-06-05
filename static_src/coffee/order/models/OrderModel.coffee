define [
  'BaseModel'
],
(BaseModel) ->


  class OrderModel extends BaseModel

    defaults:
      location: null
      meals   : []



  # exports
  OrderModel