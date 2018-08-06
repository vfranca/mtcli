class Candle(object):

    __ohlc = []
    open = 0
    close = 0
    max = 0
    min = 0
    upper_shadow = 0
    lower_shadow = 0
    real_body = 0
    size = 0
    
    def __init__(self, ohlc):
        self.__set_ohlc(ohlc)
        self.open = self.__get_open()
        self.close = self.__get_close()
        self.max = self.__get_max()
        self.min = self.__get_min()
        self.upper_shadow = self.__get_upper_shadow()
        self.lower_shadow = self.__get_lower_shadow()
    
    def __set_ohlc(self, ohlc):
        for part in ["Abr", "Max", "Min", "Fch"]:
            ohlc = ohlc.replace(part, "")
        ohlc = ohlc.replace(".00", ".00 ")
        ohlc = ohlc.strip()
        self.__ohlc = ohlc.split()
    
    def __get_open(self):
        return float(self.__ohlc[0])
    
    def __get_close(self):
        return float(self.__ohlc[3])
    
    def __get_max(self):
        return float(self.__ohlc[1])
    
    def __get_min(self):
        return float(self.__ohlc[2])
    
    def __get_upper_shadow(self):
        """ Se o corpo real for negativo a sombra superior é a diferença do preço máximo e a abertura """
        if self.open > self.close:
            upper_shadow = self.max - self.open
        upper_shadow = self.max - self.close
        return int(upper_shadow)
    
    def __get_lower_shadow(self):
        """ Se o corpo real for negativo a sombra inferior será a diferença do preço mínimo e o fechamento """
        if self.open > self.close:
            lower_shadow = self.min - self.close
        lower_shadow = self.open - self.min
        return int(lower_shadow)

