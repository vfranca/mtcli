
class Price():
    h = 0
    l = 0
    d = ""
    v = 0
    m = 0
    f = 0
    a = 0
    
    def __init__(self, high, low, direction):
        self.h = high
        self.l = low
        self.d = str(direction)
        self.v = self.range()
        self.m = self.medio()
        self.f = self.fibo()
        self.a = self.extension()
    
    def range(self):
        return self.h - self.l
    
    def medio(self):
        return self.l + self.v / 2
        
    def fibo(self):
        if self.d == "h":
            return self.h - self.v * 0.618
        elif self.d == "l":
            return self.l + self.v * 0.618
    
    def extension(self):
        if self.d == "h":
            return self.m + self.v
        elif self.d == "l":
            return self.m - self.v




