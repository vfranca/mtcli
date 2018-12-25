class Ohlc(object):

    open = 0
    high = 0
    low = 0
    close = 0
    
    def __init__(self, ohlc):
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])

