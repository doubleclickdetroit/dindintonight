define [
  'BaseModel'
],
(BaseModel) ->


  class MealModel extends BaseModel

    defaults:
      qty: 0


    url: ->
      attrs = @attributes.resource_uri


    parse: (attrs) ->
      attrs.meal


    addQty: ->
      qty = @get 'qty'
      @set 'qty', ++qty


    removeQty: ->
      qty = @get 'qty'
      @set 'qty', --qty if qty > 0



  # exports
  MealModel