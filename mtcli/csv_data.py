"""
Importa dados de CSV
"""

import csv
import pathlib


def get_data(fcsv):
    """Importa dados do arquivo CSV."""
    # Lista para armazenar as linhas do CSV
    data = []
    # Extrai os dados do CSV para popular a lista
    try:
        with open(fcsv, encoding="utf-16", newline="") as f:
            lines = csv.reader(f, delimiter=",", quotechar="'")
            for line in lines:
                data.append(line)
    except:
        fcsv = pathlib.Path(fcsv)
        print("Grafico %s nao encontrado! Tente novamente" % fcsv.stem)
    # Retorna a lista de listas do CSV
    return data
