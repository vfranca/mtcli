lbl_body_doji = "doji"
lbl_body_bull = "branco"
lbl_body_bear = "preto"
lbl_tail_top = "top"
lbl_tail_bottom = "bottom"
lbl_tail_none = "none"

class BrooksPatterns1(object):

    body_doji_max = 10
    
    def __init__(self, body, top, bottom):
        self.body = body
        self.top = top
        self.bottom = bottom
        self.body_pattern = self.__get_body_pattern()
        self.tail = self.__get_tail()
        self.pattern = self.__get_pattern()

    def __get_body_pattern(self):
    """ Padrão de corpo: alta/baixa/doji."""
    if abs(self.body) <= self.body_doji_max:
        return lbl_body_doji
    if self.body > 0:
        return lbl_body_bull
    if self.body < 0:
        return lbl_body_black

    def __get_tail(self):
        """Sombra menor: top/bottom/none."""
        if self.top < self.bottom:
            return lbl_tail_top
        if self.bottom < self.top:
            return lbl_tail_bottom
        return lbl_tail_none

    def __get_pattern(self):
        """ Padrão de uma barra: careca/topo raspado, fundo raspado."""
        pass
    
    def __is_topo_careca(self):
        """ Se for topo careca retorna true."""
        pass
    
    def __is_fundo_careca(self):
        """ Se for fundo careca retorna true."""
        pass
    
    def __is_careca(self):
        """ Se for careca retorna true."""
        pass
    
    def __is_bullstrong(self):
        """ Se tiver força compradora retorna true."""
        pass
    
    def __is_bearstrong(self):
        """ Se tiver força vendedora retorna true."""
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


