class Candle(object):

    open = 0
    high = 0
    low = 0
    close = 0
    upper_shadow = 0
    lower_shadow = 0
    real_body = 0
    size = 0
    
    def __init__(self, ohlc):
        self.time = ohlc[0]
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])
        self.size = self.__get_size()
        self.real_body = self.__get_real_body()
        self.upper_shadow = self.__get_upper_shadow()
        self.lower_shadow = self.__get_lower_shadow()
        self.trend = self.__get_trend()
    
    def __get_size(self):
        h = self.high
        l = self.low
        return h - l
    
    def __get_real_body(self):
        o = self.open
        c = self.close
        return c - o
    
    def __get_upper_shadow(self):
        h = self.high
        o =self.open
        c = self.close
        
        if c >= o:
            upper_shadow = h -c
        else:
            upper_shadow = h - o
        
        return upper_shadow
    
    def __get_lower_shadow(self):
        l = self.low
        o =self.open
        c = self.close
        
        if c >= o:
            lower_shadow = o - l
        else:
            lower_shadow = c - l
        
        return lower_shadow
    
    def __get_trend(self):
        rb =self.real_body
        
        if rb > 0:
            trend = "alta"
        elif rb < 0:
            trend = "baixa"
        else:
            trend = "lateral"
        
        return trend
    
    def high_trend_low(self):
        h = str(self.high)
        l = str(self.low)
        t = self.trend
        return t + " " + h + " " + l
    
