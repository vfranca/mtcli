lbl_bullreversal = "reversao"
lbl_bearreversal = "reversao"
lbl_microdoubletop = "microtopoduplo"
lbl_microdoublebottom = "microfundoduplo"

class BrooksPatterns2(object):

    def __init__(self, body, open, close):
        self.body = body
        self.open = open
        self.close = close
        self.pattern = self.__get_pattern()

    def __get_pattern(self):
        """ Padrão de duas barras."""
        bull_rev = bull_reversal(body, open, close)
        bear_rev = bear_reversal(body, open, close)
    
        if bull_rev:
            return bull_rev
        if bear_rev:
            return bear_rev
        return ""

    def __is_bull_reversal(self):
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
    
    def __is_bear_reversal(self):
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
    
    def __is_microdoubletop(self):
        """Se for micro topo duplo retorna true."""
        pass

    def __is_microdoublebottom(self):
        """Se for micro fundo duplo retorna true."""
        pass

