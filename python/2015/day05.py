from aoc import run_solver
import re


def is_nice(s):
    if any(pair in s for pair in ["ab", "cd", "pq", "xy"]):
        return False
    vowels = sum(1 for c in s if c in "aeiou")
    if vowels < 3:
        return False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            break
    else:
        return False
    return True


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    return str([is_nice(line) for line in lines].count(True))


def is_really_nice(s):
    double_pair = r'(\w\w).*\1'
    split_pair = r'(\w)\w\1'
    if re.search(double_pair, s) is None:
        return False
    if re.search(split_pair, s) is None:
        return False
    return True

def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    return str([is_really_nice(line) for line in lines].count(True))


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
