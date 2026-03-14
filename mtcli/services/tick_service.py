"""
TickService

Inicializa:

- TickEngine
- MaintenanceService
"""

from mtcli.marketdata.tick_engine import TickEngine
from mtcli.services.maintenance_service import MaintenanceService

_engine = None
_maintenance = None


def ensure_tick_engine(symbols):

    global _engine
    global _maintenance

    if _engine:
        return _engine

    _engine = TickEngine(symbols)

    _engine.start()

    # inicia manutenção automática
    _maintenance = MaintenanceService()
    _maintenance.start()

    return _engine
