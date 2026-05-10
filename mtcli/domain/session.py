from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    name: str
    start_hour: int
    end_hour: int

    def contains(self, hour: int) -> bool:
        return self.start_hour <= hour < self.end_hour
