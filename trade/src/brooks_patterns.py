
class BrooksPatterns(object):

    body_doji_bar = 50
    

    def __init__(self, body):
        self.body = body
        self.pattern = self.__get_pattern()
    
    def __str__(self):
        pass
    
    def __get_pattern(self):
        #btrb = self.body_trend_range_bar
        #body = self.body
        if abs(self.body) > self.body_doji_bar:
            if self.body > 0:
                return "alta"
            elif self.body < 0:
                return "baixa"
        return "doji"
        