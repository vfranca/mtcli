class Fibo(object):
    def __init__(self, high, low, trend):
        self.h = high
        self.l = low
        self.d = str(trend)
        self.range = self.__get_range()
        self.r = self.__get_retracao()
        self.r61 = self.__get_retracao_61()
        self.e = self.__get_extension()
    
    def __get_range(self):
        return self.h - self.l
    
    def __get_retracao(self):
        return self.l + self.range / 2
        
    def __get_retracao_61(self):
        if self.d == "h":
            return self.h - self.range * 0.618
        elif self.d == "l":
            return self.l + self.range * 0.618
    
    def __get_extension(self):
        if self.d == "h":
            return self.r + self.range
        elif self.d == "l":
            return self.r - self.range




