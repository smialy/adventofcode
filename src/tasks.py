from pathlib import Path
from aocd import get_data

from .models import InputTask


class TaskReader:
    def __init__(self, path: Path) -> None:
        self.path = path

    def get(self, year: int, day: int):
        sday = f"{day:02}"
        path = self.path / str(year) / sday
        input_path = path / 'input.txt'
        result_path = path / "result.txt"
        if not path.exists():
            path.mkdir(parents=True)
        if not input_path.exists():
            data = get_data(year=year, day=day)
            input_path.write_text(data)
        if not result_path.exists():
            result_path.write_text("\n\n")
        return InputTask(year, day, input_path.read_text(), result_path.read_text())


