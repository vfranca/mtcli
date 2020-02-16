class View(object):
    def show_list(self, list):
        raise NotImplementedError


class DefaultView(View):
    def show_list(self, bars):
        res = ""
        for bar in bars:
            res += bar + "\n"
        return res
