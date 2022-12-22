import csv


class Data:

    data = []

    def __init__(self, csv_file):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.data)


class Rates(Data):
    def __init__(self, csv_file):
        with open(csv_file, encoding="utf-16", newline="") as f:
            lines = csv.reader(f, delimiter=",", quotechar="'")
            for line in lines:
                self.data.append(line)

    def __iter__(self):
        for item in self.data:
            yield item
