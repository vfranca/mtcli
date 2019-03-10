
body_doji_max = 10

def get_body(body):
    """ Tipo do corpo: branco/preto/doji."""
    if abs(body) <= body_doji_max:
        return "doji"
    if body > 0:
        return "branco"
    if body < 0:
        return "preto"

def get_tail(top, bottom):
    """Sombra menor: topo/fundo/neutro."""
    if top < bottom:
        return "top"
    if bottom < top:
        return "bottom"
    return "neutro"

def get_pattern1(body, top, bottom):
    """ Padrão de uma barra: careca/topo raspado, fundo raspado."""
    pass

def bull_reversal(body, open, close):
    """ Verifica se existe reversão de alta de duas barras."""
    b1 = body[0]
    o1 = open[0]
    o2 = open[1]
    c1 = close[0]
    c2 = close[1]
    b2 = body[1]
    signal = ""
    
    if b1 >= 0:
        return False
    if b2 <= 0:
        return False
    #signal = "reversao alta"
    
    if o2 <= c1:
        signal += ""
    if c2 > c1:
        signal += "reversao alta"
    
    return signal

def bear_reversal(body, open, close):
    """ Verifica se existe reversão de baixa de duas barras."""
    b1 = body[0]
    o1 = open[0]
    o2 = open[1]
    c1 = close[0]
    c2 = close[1]
    b2 = body[1]
    signal = ""
    
    if b1 <= 0:
        return False
    if b2 >= 0:
        return False
    #signal = "reversao baixa"
    
    if o2 >= c1:
        signal += ""
    if c2 < c1:
        signal += "reversao baixa"
    
    return signal

def get_pattern2(body, open, close):
    """Padrão de duas barras: reversão de alta/reversão de baixa."""
    bull_rev = bull_reversal(body, open, close)
    bear_rev = bear_reversal(body, open, close)
    
    if bull_rev:
        return bull_rev
    if bear_rev:
        return bear_rev
    return ""


