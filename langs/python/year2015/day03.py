import sys
from collections import Counter

dirs = {
    "^": (1,0),
    ">": (0, 1),
    "v": (-1, 0),
    "<": (0, -1),
}

def resolve(chars: str):
    current = (0, 0)
    house = Counter()
    house[current] += 1
    for char in chars:
        direction = dirs[char]
        current = current[0] + direction[0], current[1] + direction[1]
        house[current] += 1
   
    robo = 0
    currents = [(0, 0), (0, 0)]
    houses = Counter()
    houses[currents[0]] += 2
    for char in chars:
        direction = dirs[char]
        current = currents[robo]
        current = current[0] + direction[0], current[1] + direction[1]
        houses[current] += 1
        currents[robo] = current
        robo = 0 if robo else 1
    

    return len(house), len(houses)

if __name__ == "__main__":
    a, b = resolve(sys.stdin.read())
    print(f"{a}")
    print(f"{b}")
