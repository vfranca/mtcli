"""
Padrões de Candlesticks
"""


# Padrões simples

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
    """ Se existir martelo retorna True."""
    # Se o corpo é de um doji retorna False
    if abs(body) <= doji_body_max:
        return False
    # Se a sombra inferior for menor que 67% retorna False
    if bottom < 67:
        return False
    return True


def is_inverted_hammer(body, top, bottom):
    """ Se existir martelo invertido retorna True."""
    # Se o corpo é de um doji retorna False
    if abs(body) <= doji_body_max:
        return False
    # Se a sombra superior for menor que 67% retorna False
    if top < 67:
        return False
    return True


def get_pattern(body, top, bottom):
    """Retorna o padrão existente no candle."""
    # Verifica se é doji
    if is_doji(body, top, bottom):
        return "doji"
    # Verifica se é doji de alta
    if is_bullish_doji(body, top, bottom):
        return "doji alta"
    # Verifica se é doji dragão voador
    if is_dragon_fly_doji(body, top, bottom):
        return "doji dragão"
    # Verifica se é doji de baixa
    if is_bearish_doji(body, top, bottom):
        return "doji baixa"
    # Verifica se é doji lápide
    if is_gravestone_doji(body, top, bottom):
        return "doji lápide"
    # Verifica se é doji de quatro preços
    if is_four_prices_doji(body, top, bottom):
        return "doji quat pre"
    # Verifica se é marubozu
    if is_marubozu(body, top, bottom):
        return "marubozu"
    # Verifica se é spinning top
    if is_spinning_top(body, top, bottom):
        return "spin top"
    # Verifica se é martelo/enforcado
    if is_hammer(body, top, bottom):
        return "martelo"
    # Verifica se é martelo invertido/estrela cadente
    if is_inverted_hammer(body, top, bottom):
        return "martinvert"
    return ""


# Padrões de dois candles


def is_star(body, open, close):
    pass


def is_doji_star(body, open, close):
    pass


def is_bullish_engolfing(body, open, close):
    """ Se existir engolfo de alta retorna True."""
    if body[1] > 0 and body[0] < 0:
        if open[1] <= close[0] and close[1] >= open[0]:
            return True
    return False


def is_bearish_engolfing(body, open, close):
    """ Se existir engolfo de baixa retorna True."""
    if body[1] < 0 and body[0] > 0:
        if open[1] >= close[0] and close[1] <= open[0]:
            return True
    return False


def is_black_cloud_cover(body, open, close):
    pass


def is_piersing_line(body, open, close):
    pass


def get_two_candles_pattern(body, open, close):
    """Verifica padrões de dois candles."""
    if is_bullish_engolfing(body, open, close):
        return "engolfo"
    if is_bearish_engolfing(body, open, close):
        return "engolfo"
    return ""
