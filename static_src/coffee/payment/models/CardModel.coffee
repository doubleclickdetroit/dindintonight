define [
  'BaseModel'
],
(BaseModel) ->


  class CardModel extends BaseModel

    defaults:
      name_first    : null
      name_last     : null
      address_line1 : null
      address_city  : null
      address_state : null
      address_zip   : null


    parse: (attrs) ->
      return attrs unless attrs.card?
      @sandbox.util.extend attrs.card, { token: attrs.id }


    reset: (attrs={}) ->
      attrs = @sandbox.util.extend {}, @defaults, attrs
      @clear { silent: true }
      @set attrs, { silent: true }


    validate: (attrs) ->
      for key, val of attrs
        error = @displayError key unless val?
        break if error?

      error


    displayError: (key) ->
      switch key
        when 'name_first','name_last'                                     then 'Your name is required.'
        when 'address_line1','address_city','address_state','address_zip' then 'Your address is required.'



  CardModel