from mtcli.database import get_connection
from .runner import run_migrations


conn = get_connection()
run_migrations(conn)

