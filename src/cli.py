import argparse
import datetime
from pathlib import Path

from .runners import PythonRunner
from .tasks import TaskReader
from .resolvers import create_default_resolver

ROOT = Path(__file__).parent.parent
LANGS = ROOT / "langs"
INPUTS = ROOT / "inputs"


def filter_jobs(jobs: list, year: int|None, day: int|None):
    for job in jobs:
        if year is None or year == job.year and day is None or day == job.day:
            yield job


def cli():
    now = datetime.datetime.now()
    years = range(2015, now.year + int(now.month == 12))
    parser = argparse.ArgumentParser(
        description=f"My Advent of Code",
        usage=f"aocd [year 2015-{years[-1]}] [day 1-25] ",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "year",
        nargs="?",
        type=int,
        help=f"2015-{years[-1]} (default: %(default)s)",
    )
    parser.add_argument(
        "day",
        nargs="?",
        type=int,
        help="1-25 (default: %(default)s)",
    )
    args = parser.parse_args()

    resolvers = create_default_resolver(LANGS)
    tasks = TaskReader(INPUTS)
    py_runner = PythonRunner()
    for job in filter_jobs(resolvers.read(), args.year, args.day):
        task = tasks.get(job.year, job.day)
        result = py_runner.run(job, task)
        print(f"{job.kind}::{task.year}/{task.day:02}")
        print(result)
        if result.strip() == task.result.strip():
            print("OK")
        else:
            print("Expected: ", task.result.strip().split("\n"))
            print("Result: ", result.split("\n"))


