define [
  'backbone'
],
(Backbone) ->


  class CardsCollection extends Backbone.Collection


    initialize: ->
      @on 'change:selected', @selectCard, @


    selectCard: (card_model) ->
      cards = @without( card_model )
      @sandbox.util.each cards, (card) ->
        card.set 'selected', false, silent: true



  # exports
  CardsCollection