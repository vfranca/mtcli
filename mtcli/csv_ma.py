# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import csv


class MAs:

    data = []

    def __init__(self, csv_file):
        with open(csv_file, encoding="utf-16", newline="") as f:
            lines = csv.reader(f, delimiter=",", quotechar="'")
            for line in lines:
                self.data.append(line)

    def __iter__(self):
        for item in self.data:
            yield item
