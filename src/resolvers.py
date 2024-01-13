import os
from pathlib import Path

from .models import Job


class PythonResolver:
    def __init__(self, root: Path) -> None:
        self.root = root 

    def read(self):
        for root, dirs, files in os.walk(self.root):
            for file in files:
                if file.startswith("day"):
                    yield Job("python", Path(root) / file, int(root[-4:]), int(file[3:-3]))

class Resolvers:
    def __init__(self, resolvers) -> None:
        self.resolvers = resolvers

    def read(self):
        for resolver in self.resolvers:
            yield from resolver.read()


def create_default_resolver(root: Path):
    return Resolvers([
        PythonResolver(root / "python")
    ])
