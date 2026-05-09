"""
Factory de DataSources.

Responsável por instanciar fontes de dados sem acoplamento
e evitando import circular.
"""


def create_data_source(name: str):
    """
    Cria uma fonte de dados a partir do nome.

    Args:
        name (str): "mt5" ou "csv"

    Returns:
        DataSourceBase
    """
    name = (name or "mt5").lower()

    if name == "mt5":
        from mtcli.data.mt5 import MT5DataSource
        return MT5DataSource()

    if name == "csv":
        from mtcli.data.csv import CsvDataSource
        return CsvDataSource()

    raise ValueError(f"Fonte de dados desconhecida: {name}")
