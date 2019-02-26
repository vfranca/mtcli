
class BrooksPatterns(object):

    body_doji_bar = 10
    

    def __init__(self, body, top, bottom):
        self.body = body
        self.top = top
        self.bottom = bottom
        self.pattern = self.__get_pattern()
        self.color = self.__get_color()
        self.tail = self.__get_tail()
    
    def __str__(self):
        pass
    
    def __get_pattern(self):
        if abs(self.body) > self.body_doji_bar:
            if self.body > 0:
                return "branco"
            elif self.body < 0:
                return "preto"
        return "doji"
    
    def __get_color(self):
        if self.body > 0:
            return "verde"
        elif self.body < 0:
            return "vermelho"
        return ""
    
    def __get_tail(self):
        if self.top > self.bottom:
            return "bottom"
        if self.bottom > self.top:
            return "top"
        return ""
    
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
    signal = "reversao alta"
    
    if o2 <= c1:
        signal += "+"
    if c2 > c1:
        signal += "+"
    
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
    signal = "reversao baixa"
    
    if o2 >= c1:
        signal += "+"
    if c2 < c1:
        signal += "+"
    
    return signal

def get_pattern_bars(body, open, close):
    """Verifica padrões de duas barras."""
    bull_rev = bull_reversal(body, open, close)
    bear_rev = bear_reversal(body, open, close)
    
    if bull_rev:
        return bull_rev
    if bear_rev:
        return bear_rev
    return ""


