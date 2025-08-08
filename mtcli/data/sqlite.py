import sqlite3
import pandas as pd
from mtcli import conf
from .base import DataSourceBase


class SqliteDataSource(DataSourceBase):
    """Fonte de dados via banco de dados SQLite."""

    def get_data(self, symbol, period):
        conn = sqlite3.connect(conf.sqlite_path)
        query = "SELECT * FROM rates WHERE symbol = ? AND period = ? ORDER BY time"
        df = pd.read_sql(query, conn, params=(symbol, period))
        conn.close()
        return df.to_dict(orient="records")
