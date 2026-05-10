from dataclasses import dataclass


@dataclass(frozen=True)
class Price:
    value: float
    digits: int

    def normalize(self) -> float:
        return round(self.value, self.digits)

    def points(self, other: "Price") -> float:
        return (self.value - other.value) * (10 ** self.digits)
