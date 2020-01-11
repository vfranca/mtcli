# -*- coding: utf-8 -*-
import csv


def bar_model(file):
    """ Lê um gráfico de barras/candlestick para uma lista."""
    f = open(file, encoding="utf-16", newline="")
    lines = csv.reader(f, delimiter=",", quotechar="'")
    r = []
    for line in lines:
        r.append(line)
    f.close()
    return r
