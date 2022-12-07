from aoc import run_solver


def part1(input_str: str) -> str:
    for i in range(len(input_str) - 4):
        if len(set(input_str[i : i + 4])) == 4:
            return i + 4

    return "No marker found"


def part2(input_str: str) -> str:
    for i in range(len(input_str) - 14):
        if len(set(input_str[i : i + 14])) == 14:
            return i + 14

    return "No marker found"


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
