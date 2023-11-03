import sys
import hashlib


def resolve(word: str):
    i = 0
    first = 0
    while True:
        i += 1
        hash = hashlib.md5(f"{word}{i}".encode()).hexdigest()
        if not first and hash[:5] == '00000':
            first = i
        elif hash[:6] == '000000':
            return first, i 


if __name__ == "__main__":
    a, b = resolve(sys.stdin.read().strip())
    print(f"{a}")
    print(f"{b}")
