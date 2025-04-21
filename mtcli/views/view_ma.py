class MaView:

    def __init__(self, mas):
        self.mas = mas

    def view(self):
        for ma in self.mas:
            view = "%s %.2f" % (ma.inclinacao, ma.ma)
        return view
