
class BrooksPatterns(object):

    body_trend_range_bar = 40
    

    def __init__(self, body):
        self.body = body
        self.trend = self.__get_trend()
    
    def __str__(self):
        pass
    
    def __get_trend(self):
        btrb = self.body_trend_range_bar
        body = self.body
        if abs(body) > btrb:
            if body > 0:
                return "alta"
            elif body < 0:
                return "baixa"
        return "lateral"
        