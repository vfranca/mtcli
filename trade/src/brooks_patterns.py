
class BrooksPatterns(object):

    body_doji_bar = 10
    

    def __init__(self, body, top, bottom):
        self.body = body
        self.top = top
        self.bottom = bottom
        self.pattern = self.__get_pattern()
        self.color = self.__get_color()
        self.tail = self.__get_tail()
    
    def __str__(self):
        pass
    
    def __get_pattern(self):
        if abs(self.body) > self.body_doji_bar:
            if self.body > 0:
                return "branco"
            elif self.body < 0:
                return "preto"
        return "doji"
    
    def __get_color(self):
        if self.body > 0:
            return "verde"
        elif self.body < 0:
            return "vermelho"
        return ""
    
    def __get_tail(self):
        if self.top > self.bottom:
            return "bottom"
        if self.bottom > self.top:
            return "top"
        return ""
    
        