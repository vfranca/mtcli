"""
View base
"""


class View(object):

    view = ""

    def __init__(self, data_set):
        self.data_set = data_set
        self.set()

    def set(self):
        pass
