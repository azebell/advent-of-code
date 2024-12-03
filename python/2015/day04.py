from aoc import run_solver
import hashlib


def part1(input_str: str) -> str:
    answer = 1
    key = input_str.strip()
    while True:
        h = hashlib.md5((key + str(answer)).encode("utf-8")).hexdigest()
        if h.startswith("00000"):
            break
        answer += 1
    return str(answer)


def part2(input_str: str) -> str:
    answer = 1
    key = input_str.strip()
    while True:
        h = hashlib.md5((key + str(answer)).encode("utf-8")).hexdigest()
        if h.startswith("000000"):
            break
        answer += 1
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
