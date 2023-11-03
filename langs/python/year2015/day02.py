import sys
import functools

def resolve(lines: list[str]):
    area = 0
    rib = 0
    for line in lines:
        dim = [int(n) for n in line.split("x")]
        length, width, height = dim
        area_length, area_width, area_height = length*width, width*height, height*length
        area += 2 * (area_length + area_width + area_height)
        area += min(area_length, area_width, area_height)
        rib += sum(sorted(dim)[:2])*2 + functools.reduce(lambda a,b: a*b, dim)
        
    return area, rib

if __name__ == "__main__":
    a, b = resolve(sys.stdin.read().split("\n"))
    print(f"{a}")
    print(f"{b}")
