
class Candle(object):

    def __init__(self, ohlc):
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])
        self.datetime = ohlc[0]
        self.date = self.__get_date()
        self.size = self.__get_size()
        self.body = self.__get_body()
        self.top_tail = self.__get_top_tail()
        self.bottom_tail = self.__get_bottom_tail()
        self.trend = self.__get_trend()
    
    def __get_size(self):
        """ Retorna o tamanho da barra."""
        h = self.high
        l = self.low
        return h - l
    
    def __get_body(self):
        """ Retorna o tamanho  proporcional do corpo."""
        o = self.open
        c = self.close
        s = self.size
        if s == 0:
            return 0
        
        return round((c - o) / s, 2)
    
    def __get_top_tail(self):
        """ Retorna a calda superior proporcional ao tamanho da barra."""
        h = self.high
        o =self.open
        c = self.close
        s = self.size
        
        if c >= o:
            top_tail = h -c
        else:
            top_tail = h - o
        
        if s == 0:
            return 0
        
        return round(top_tail / s, 2)
    
    def __get_bottom_tail(self):
        """ Retorna a calda inferior proporcional ao tamanho da barra."""
        l = self.low
        o =self.open
        c = self.close
        s = self.size
        
        if c >= o:
            bottom_tail = o - l
        else:
            bottom_tail = c - l
        
        if s == 0:
            return 0
        
        return round(bottom_tail / s, 2)
    
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
        h = round(self.high, 2)
        l = round(self.low, 2)
        c = round(self.close, 2)
        t = self.trend
        b = str(int(self.body * 100))
        return b + " " + str(h) + " " + str(l) + " " + str(c)

    def __get_date(self):
        date = self.datetime.split(' ')
        return date[0]
    
