import csv

def chart_reader(filename):
    f = open(filename, encoding = "utf-16", newline = "")
    r = csv.reader(f, delimiter = ',', quotechar = '\'')
    #f.close()
    return r
