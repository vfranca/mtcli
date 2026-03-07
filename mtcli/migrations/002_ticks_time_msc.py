def column_exists(conn, table, column):

    cursor = conn.execute(f"PRAGMA table_info({table})")

    for row in cursor.fetchall():
        if row[1] == column:
            return True

    return False


def upgrade(conn):

    if not column_exists(conn, "ticks", "time_msc"):

        conn.execute("""
        ALTER TABLE ticks
        ADD COLUMN time_msc INTEGER
        """)

    conn.commit()
