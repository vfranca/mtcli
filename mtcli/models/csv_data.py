"""Módulo de importação de arquivo CSV."""

import csv
import pathlib


def get_data(fcsv):
    """Importa dados do arquivo CSV."""
    data = []  # lista contendo as linhas do CSV
    try:
        with open(fcsv, encoding="utf-16", newline="") as f:
            lines = csv.reader(f, delimiter=",", quotechar="'")
            for line in lines:
                data.append(line)
    except:
        fcsv = pathlib.Path(fcsv)
        print("%s nao encontrado! Tente novamente" % fcsv.stem)
    # Retorna a lista de listas do CSV
    return data
