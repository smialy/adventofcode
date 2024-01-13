from dataclasses import dataclass
import sys
import numpy as np
from collections import namedtuple

@dataclass
class Not:
    reg: str

    def eval(self, regs):
        return not regs[self.reg]
    
@dataclass
class And:
    reg1: str
    reg2: str
    
    def eval(self, regs):
        return regs[self.reg1] and regs[self.reg2]


@dataclass
class Or:
    reg1: str
    reg2: str
    
    def eval(self, regs):
        return regs[self.reg1] or regs[self.reg2]

@dataclass
class RShift:
    reg: str
    value: int
    
    def eval(self, regs):
        return regs[self.reg] >> self.value

@dataclass
class LShift:
    reg: str
    value: int
    
    def eval(self, regs):
        return regs[self.reg] << self.value
    
def parse_line(line: str):
    match line.split(' '):
        case ["NOT", r1, '->', dest]:
            return (Not(r1), dest)
        case [r1, "AND", r2, "->", dest]:
            return (And(r1, r2), dest)
        case [r1, "OR", r2, "->", dest]:
            return (And(r1, r2), dest)
        case [r1, "RSHIFT", value, "->", dest]:
            return (RShift(r1, int(value)), dest)
        case [r1, "LSHIFT", value, "->", dest]:
            return (LShift(r1, int(value)), dest)
        case _:
            raise TypeError(line)


def parse_lines(lines: list[str]):
    for line in lines:
        yield parse_line(line)

if __name__ == "__main__":
    for i, (cmd, dest) in enumerate(parse_lines(lines)):
        print(i, cmd)
    print(f"{a}")
    print(f"{b}")
