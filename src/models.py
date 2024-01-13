from pathlib import Path
from dataclasses import dataclass

@dataclass
class Job:
    kind: str
    path: Path
    year: int
    day: int


@dataclass
class InputTask:
    year: int
    day: int
    data: str
    result: str

