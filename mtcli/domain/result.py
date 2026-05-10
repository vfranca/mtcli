from dataclasses import dataclass


@dataclass
class Result:
    success: bool
    data: any = None
    error: str | None = None
