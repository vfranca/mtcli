class Ohlc(object):

    def __init__(self, ohlc):
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])
        self.datetime = ohlc[0]
        self.date = self.__get_date()
    
    def __get_date(self):
        date = self.datetime.split(' ')
        return date[0]

