from aoc import run_solver


def part1(input_str: str) -> str:
    up = input_str.count("(")
    down = input_str.count(")")
    return f"{up - down}"


def part2(input_str: str) -> str:
    floor = 0
    position = 1
    for c in input_str:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            break
        position += 1
    return str(position)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
