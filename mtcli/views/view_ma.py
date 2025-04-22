class MaView:

    def __init__(self, mas, date, time):
        self.mas = mas
        self.date = date
        self.time = time + ":00" if time else ""

    def view(self):
        ma = 0
        for _ma in self.mas:
            if str(_ma.date) == self.date and not self.time:
                ma = _ma.ma
                inclinacao = _ma.inclinacao
            if str(_ma.date) == self.date and str(_ma.time) == self.time:
                ma = _ma.ma
                inclinacao = _ma.inclinacao
                break
        if not ma:
            mas = self.mas[-1:]
            for _ma in mas:
                ma = _ma.ma
                inclinacao = _ma.inclinacao
        return "%s %.2f" % (inclinacao, ma)
