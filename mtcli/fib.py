class Fib(object):
    def __init__(self, high, low, trend="h"):
        self.h = high
        self.l = low
        self.t = str(trend)
        self.range = self.__get_range()
        self.r38 = self.__retracao(0.382)
        self.r = self.__retracao(0.5)
        self.r61 = self.__retracao(0.618)
        self.e61 = self.__extension(0.618)
        self.e = self.__extension(0.5)
        self.e38 = self.__extension(0.382)

    def __get_range(self):
        return self.h - self.l

    def __retracao(self, ret):
        if self.t == "h":
            return self.h - self.range * ret
        elif self.t == "l":
            return self.l + self.range * ret

    def __extension(self, ext):
        if self.t == "h":
            return self.h + self.range * ext
        elif self.t == "l":
            return self.l - self.range * ext

    def __str__(self):
        return "%.2f %.2f %.2f > %.2f %.2f %.2f" % (
            self.r61,
            self.r,
            self.r38,
            self.e38,
            self.e,
            self.e61,
        )
