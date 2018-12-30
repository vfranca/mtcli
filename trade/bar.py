from .ohlc import Ohlc

class Bar(Ohlc):

    upper_shadow = 0
    lower_shadow = 0
    body = 0
    size = 0
    
    def __init__(self, ohlc):
        super().__init__(ohlc)
        self.size = self.__get_size()
        self.body = self.__get_body()
        self.upper_shadow = self.__get_upper_shadow()
        self.lower_shadow = self.__get_lower_shadow()
        self.trend = self.__get_trend()
    
    def __get_size(self):
        """ Retorna o tamanho do candle em ticks."""
        h = self.high
        l = self.low
        return h - l
    
    def __get_body(self):
        """ Retorna o tamanho  do corpo real proporcionalmente."""
        o = self.open
        c = self.close
        s = self.size
        if s == 0:
            return 0
        
        return round((c - o) / s, 2)
    
    def __get_upper_shadow(self):
        """ Retorna a sombra superior proporcionalmente ao tamanho do candle."""
        h = self.high
        o =self.open
        c = self.close
        s = self.size
        
        if c >= o:
            upper_shadow = h -c
        else:
            upper_shadow = h - o
        
        if s == 0:
            return 0
        
        return round(upper_shadow / s, 2)
    
    def __get_lower_shadow(self):
        """ Retorna a sombra inferior proporcionalmente ao tamanho do candle."""
        l = self.low
        o =self.open
        c = self.close
        s = self.size
        
        if c >= o:
            lower_shadow = o - l
        else:
            lower_shadow = c - l
        
        if s == 0:
            return 0
        
        return round(lower_shadow / s, 2)
    
    def __get_trend(self):
        b =self.body
        
        if b > 0:
            trend = "alta"
        elif b < 0:
            trend = "baixa"
        else:
            trend = "lateral"
        
        return trend
    
    def __str__(self):
        h = str(round(self.high))
        l = str(round(self.low))
        c = str(round(self.close))
        t = self.trend
        b = str(int(self.body * 100))
        return b + " " + h + " " + l + " " + c
    
