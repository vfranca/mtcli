"""
Importa dados de CSV
"""

import csv


def get_data(csv_file):
    """Importa dados do arquivo CSV."""
    # Lista para armazenar as linhas do CSV
    data = []
    # Extrai os dados do CSV para popular a lista
    with open(csv_file, encoding="utf-16", newline="") as f:
        lines = csv.reader(f, delimiter=",", quotechar="'")
        for line in lines:
            data.append(line)
    # Retorna a lista de listas do CSV
    return data
