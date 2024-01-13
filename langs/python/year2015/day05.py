import sys
import re

vowel_re = re.compile(r"[aeiou]")
exclude_re = re.compile(r"(ab|cd|pq|xy)")
dup_re = re.compile(r"(.)\1")

repeat_re = re.compile(r"(.).\1")
dup_pair_re = re.compile(r"(..).*\1")


def resolve(text: str, filter):
    result = 0
    i = 0
    for word in text.split("\n"):
        i+=1
        if filter(word):
            result += 1
    return result, 0


def is_nice_a(word: str) -> bool:
    if exclude_re.search(word):
        return False
    if len(vowel_re.findall(word)) < 3:
        return False
    if dup_re.search(word) is None:
        return False
    return True

def is_nice_b(word: str) -> bool:
    if repeat_re.search(word) is None:
        return False
    return dup_pair_re.search(word) is not None

if __name__ == "__main__":
    input = sys.stdin.read().strip()
    a = resolve(input, is_nice_a)
    b = resolve(input, is_nice_b)
    print(f"{a}")
    print(f"{b}")
