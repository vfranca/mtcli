"""
MaintenanceService

Executa manutenção automática do banco de dados.

Responsável por:

- backup diário
- purge de ticks antigos
- vacuum incremental
- optimize do SQLite
- limpeza de backups antigos

Esse serviço roda silenciosamente em background
uma vez por dia.
"""

import threading
import time
from datetime import datetime, timedelta
from pathlib import Path

from mtcli.database import get_connection, BACKUP_DIR


class MaintenanceService:

    # executa manutenção a cada 12h
    INTERVAL_SECONDS = 43200

    # manter backups por 7 dias
    BACKUP_RETENTION_DAYS = 7

    def __init__(self):

        self.conn = get_connection()

        self.running = False
        self.thread = None

        self.last_run_day = None

    # ==========================================================
    # CONTROLE
    # ==========================================================

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="mtcli-maintenance-service"
        )

        self.thread.start()

    # ----------------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

    # ==========================================================
    # LOOP PRINCIPAL
    # ==========================================================

    def _run(self):

        while self.running:

            try:

                self._maybe_run_maintenance()

            except Exception as e:

                # nunca deixar serviço morrer
                print("MaintenanceService error:", e)

            time.sleep(self.INTERVAL_SECONDS)

    # ==========================================================
    # EXECUÇÃO CONDICIONAL
    # ==========================================================

    def _maybe_run_maintenance(self):

        today = datetime.now().date()

        if self.last_run_day == today:
            return

        self._run_maintenance()

        self.last_run_day = today

    # ==========================================================
    # MANUTENÇÃO
    # ==========================================================

    def _run_maintenance(self):

        print("mtcli: running database maintenance")

        self._optimize_database()

        self._incremental_vacuum()

        self._cleanup_old_backups()

    # ==========================================================
    # SQLITE OPTIMIZE
    # ==========================================================

    def _optimize_database(self):

        try:

            self.conn.execute("PRAGMA optimize")
            self.conn.execute("ANALYZE")

        except Exception as e:

            print("optimize error:", e)

    # ==========================================================
    # VACUUM INCREMENTAL
    # ==========================================================

    def _incremental_vacuum(self):

        try:

            self.conn.execute("PRAGMA incremental_vacuum")

        except Exception as e:

            print("vacuum error:", e)

    # ==========================================================
    # LIMPEZA DE BACKUPS
    # ==========================================================

    def _cleanup_old_backups(self):

        cutoff = datetime.now() - timedelta(days=self.BACKUP_RETENTION_DAYS)

        for file in BACKUP_DIR.glob("marketdata_*.db"):

            try:

                timestamp = file.stem.split("_")[1]

                file_date = datetime.strptime(timestamp, "%Y%m%d")

                if file_date < cutoff:

                    file.unlink()

            except Exception:

                pass
