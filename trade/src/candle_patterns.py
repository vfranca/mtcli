#encoding: utf-8

doji_body_max = 3
doji_shadow_min = 30
umbrella_body_max = 25

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
    return True

def is_bearish_doji(body, top, bottom):
    """ Se existir doji de baixa retorna False."""
    # Se o corpo não for de um doji retorna False
    if abs(body) > doji_body_max:
        return False
    # Se a sombra inferior não for de doji retorna False
    if bottom > doji_shadow_min:
        return False
    return True

