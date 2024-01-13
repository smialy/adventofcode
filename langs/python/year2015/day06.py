import sys
import numpy as np
from collections import namedtuple


Cmd = namedtuple('Cmd', 'name,state,dim')

class Grid:
    def __init__(self) -> None:
        self.area = np.full((1000, 1000), False)

    def run(self, cmd: Cmd):
        pass

    def count(self):
        return self.area.sum()

class LightGrid(Grid):
    def __init__(self) -> None:
        self.area = np.full((1000, 1000), False)

    def run(self, cmd: Cmd):
        if cmd.name == 'turn':
            a, b = cmd.dim
            self.area[a[0]:b[0]+1, a[1]:b[1]+1] = cmd.state
        elif cmd.name == 'toggle':
            a, b = cmd.dim
            self.area[a[0]:b[0]+1, a[1]:b[1]+1] = ~self.area[a[0]:b[0]+1, a[1]:b[1]+1]
        else:
            raise TypeError(cmd)

    def count(self):
        return self.area.sum()

class DimmerLightGrid(Grid):
    def __init__(self) -> None:
        self.area = np.full((1000, 1000), 0)

    def run(self, cmd: Cmd):
        if cmd.name == 'turn':
            a, b = cmd.dim
            v = self.area[a[0]:b[0]+1, a[1]:b[1]+1] 
            if cmd.state:
                v+=1
            else:
                v[v > 0] -= 1

        elif cmd.name == 'toggle':
            a, b = cmd.dim
            self.area[a[0]:b[0]+1, a[1]:b[1]+1] += 2
        else:
            raise TypeError(cmd)

    def count(self):
        return self.area.sum()


def parse_size(size: str) -> tuple[int, int]:
    a, b = size.split(",")
    return int(a), int(b)


def parse_line(line: str):
    match line.split(' '):
        case ["toggle", d1, 'through', d2]:
            return Cmd('toggle', None, (parse_size(d1), parse_size(d2)))
        case ["turn", state, d1, 'through', d2]:
            state = True if state == 'on' else False
            return Cmd('turn', state, (parse_size(d1), parse_size(d2)))
        case _:
            raise TypeError(line)


def parse_lines(lines: list[str]):
    for line in lines:
        yield parse_line(line)


if __name__ == "__main__":
    lines = sys.stdin.read().strip().split("\n")
    grid_a = LightGrid()
    grid_b = DimmerLightGrid()
    for i, cmd in enumerate(parse_lines(lines)):
        grid_a.run(cmd)
        grid_b.run(cmd)
    a = grid_a.count()
    b = grid_b.count()
    print(f"{a}")
    print(f"{b}")
