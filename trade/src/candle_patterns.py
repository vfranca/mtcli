#encoding: utf-8

doji_body_max = 3
doji_shadow_min = 30
spinning_top_shadow_min = 40
umbrella_body_max = 25

def is_doji(body, top, bottom):
    """ Se existe o doji retorna True."""
    # Se o corpo não é de doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra superior é de doji de alta retorna False
    if top <= doji_shadow_min:
        return False
    # Se a sombra inferior é de doji de baixa retorna False
    if bottom <= doji_shadow_min:
        return False
    return True

def is_bullish_doji(body, top, bottom):
    """ Se existir doji de alta retorna True."""
    # Se o corpo não for de um doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra superior não for de um doji retorna False
    if top > doji_shadow_min:
        return False
    # Se a sombra superior for nula retorna False
    if top == 0:
        return False
    return True

def is_dragon_fly_doji(body, top, bottom):
    """ Se existir doji dragão voador retorna True."""
    # Se o corpo não for de um doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra superior for maior que 0 retorna False
    if top > 0:
        return False
    # Se não existir sombra inferior retorna False
    if bottom == 0:
        return False
    return True

def is_bearish_doji(body, top, bottom):
    """ Se existir doji de baixa retorna False."""
    # Se o corpo não for de um doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra inferior não for de doji retorna False
    if bottom > doji_shadow_min:
        return False
    # Se a sombra inferior for de um doji lápide retorna False
    if bottom == 0:
        return False
    return True

def is_gravestone_doji(body, top, bottom):
    """ Se existir doji lápide retorna True."""
    # Se o corpo não for de um doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra inferior for maior que 0 retorna False
    if bottom > 0:
        return False
    # Se não existir sombra superior retorna False
    if top == 0:
        return False
    return True

def is_four_prices_doji(body, top, bottom):
    """Se existir o doji de quatro preços retorna True."""
    # Se existir corpo retorna False
    if abs(body) > 0:
        return False
    # Se existir sombra superior retorna zero
    if top > 0:
        return False
    # Se existir sombra inferior retorna False
    if bottom > 0:
        return False
    return True

def is_marubozu(body, top, bottom):
    """Se existir marubozu retorna True."""
    # Se o corpo for 100% do candle retorna True
    if abs(body) == 100:
        return True
    return False

def is_spinning_top(body, top, bottom):
    """Se existir spinning top retorna True."""
    # Se o corpo é de doji retorna False
    if abs(body) <= doji_body_max:
        return False
    # Se a sombra superior não é de spinning top retorna False
    if top < spinning_top_shadow_min:
        return False
    # Se a sombra inferior não é de spinning top retorna False
    if bottom < spinning_top_shadow_min:
        return False
    return True

def is_hammer(body, top, bottom):
    """ Retorna True se o padrao for martelo."""
    # Se o corpo é de um doji retorna False
    if abs(body) <= doji_body_max:
        return False
        # Se a sombra superior não for de um guarda-chuva retorna False
    if top > (umbrella_body_max - doji_body_max):
        return False
    # Se o corpo não for de guarda-chuva retorna False
    if abs(body) > umbrella_body_max:
        return False
    return True

