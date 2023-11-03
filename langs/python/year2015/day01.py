import sys

def resolve(chars: str):
    final_floor = 0
    basement = -1
    for i, sign in enumerate(chars):
        final_floor += 1 if sign == "(" else -1
        if final_floor == -1 and basement == -1:
            basement = i+1
    return basement, final_floor
    
if __name__ == "__main__":
    a, b = resolve(sys.stdin.read())
    print(f"{a}\n{b}\n")
