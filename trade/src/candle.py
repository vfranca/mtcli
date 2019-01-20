
class Candle(object):

    def __init__(self, ohlc):
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])
        self.datetime = ohlc[0]
        self.date = self.__get_date()
        self.range = self.__get_range()
        self.body = self.__get_body()
        self.top_tail = self.__get_top_tail()
        self.bottom_tail = self.__get_bottom_tail()
        self.trend = self.__get_trend()
    
    def __get_range(self):
        """ Retorna o range do candle."""
        return self.high - self.low
    
    def __get_body(self):
        """ Retorna o tamanho  proporcional do corpo real em porcentagem."""
        if self.range == 0:
            return 0
        
        return round((self.close - self.open) / self.range, 2) * 100
    
    def __get_top_tail(self):
        """ Retorna a sombra superior em porcentagem proporcional ao range do candle."""
        high = self.high
        open =self.open
        close = self.close
        range = self.range
        
        if close >= open:
            top = high -close
        else:
            top = high - open
        
        if range == 0:
            return 0
        
        return round(top / range, 2) * 100
    
    def __get_bottom_tail(self):
        """ Retorna a sombra inferior em porcentagem proporcional ao range do candle."""
        low = self.low
        open =self.open
        close = self.close
        range = self.range
        
        if close >= open:
            bottom = open - low
        else:
            bottom = close - low
        
        if range == 0:
            return 0
        
        return round(bottom / range, 2) * 100
    
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
        high = self.high
        low = self.low
        close = self.close
        trend = self.trend
        body = str(int(self.body))
        return "%s %.1f %.1f %.1f" % (body, high, low, close)

    def __get_date(self):
        date = self.datetime.split(' ')
        return date[0]
    
