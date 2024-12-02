from aoc import run_solver
import re


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    answer = 0
    for line in lines:
        m = re.findall(pattern, line)
        for a, b in m:
            answer += int(a) * int(b)
    return str(answer)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    pattern = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    answer = 0
    enabled = True
    for line in lines:
        m = re.findall(pattern, line)
        for x, a, b in m:
            if x == "do()":
                enabled = True
            elif x == "don't()":
                enabled = False
            elif enabled:
                answer += int(a) * int(b)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
