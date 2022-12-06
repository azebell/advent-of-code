from aoc import run_solver


def part1(input_str: str) -> str:
    i = 0
    processed = -1
    while i + 4 <= len(input_str):
        if len(set(input_str[i : i + 4])) == 4:
            processed = i + 4
            break
        i += 1

    return str(processed)


def part2(input_str: str) -> str:
    i = 0
    processed = -1
    while i + 14 <= len(input_str):
        if len(set(input_str[i : i + 14])) == 14:
            processed = i + 14
            break
        i += 1

    return str(processed)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
