import os
import shlex
import subprocess
from pathlib import Path
from dataclasses import dataclass
from aocd import get_data

ROOT = Path(__file__).parent.parent
LANGS = ROOT / "langs"
INPUTS = ROOT / "inputs"


class PythonResolver:
    def __init__(self, path: Path) -> None:
        self.path = path
    def read(self):
        for root, dirs, files in os.walk(self.path / "python"):
            print(root, files)
            for file in files:
                if file.startswith("day"):
                    yield PythonJob(Path(root) / file, int(root[-4:]), int(file[3:-3]))


@dataclass
class PythonJob:
    path: Path
    year: int
    day: int
    kind: str = 'python'


@dataclass
class InputTask:
    year: int
    day: int
    data: str
    result: str


class PythonRunner:
    def run(self, job: PythonJob, task: InputTask):
        cmd = shlex.split(f"pdm run python {job.path}")
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        resp, _ = p.communicate(input=task.data.encode())
        return resp.decode()


class TaskResolver:
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


def main():
    tasks = TaskResolver(INPUTS)
    py_resolver = PythonResolver(LANGS)
    py_runner = PythonRunner()
    for job in py_resolver.read():
        task = tasks.get(job.year, job.day)
        result = py_runner.run(job, task)
        print(f"{job.kind}::{task.year}/{task.day:02}")
        if result.strip() == task.result.strip():
            print("OK")
        else:
            print("Expected: ", task.result.strip().split("\n"))
            print("Result: ", result.split("\n"))


if __name__ == '__main__':
    main()
