from datetime import datetime
from zoneinfo import ZoneInfo


UTC = ZoneInfo("UTC")
B3_TZ = ZoneInfo("America/Sao_Paulo")


def now_utc():
    return datetime.now(tz=UTC)


def utc_to_b3(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(B3_TZ)
