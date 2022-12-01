from aoc import run_solver


def part1(input_str: str) -> str:
    paper = 0
    for line in input_str.strip().split("\n"):
        l, w, h = map(int, line.split("x"))
        surface = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(l * w, w * h, h * l)
        paper += surface + slack
    return str(paper)


def part2(input_str: str) -> str:
    ribbon = 0
    for line in input_str.strip().split("\n"):
        dimensions = map(int, line.split("x"))
        a, b, c = sorted(dimensions)
        wrap = 2 * (a + b)
        bow = a * b * c
        ribbon += wrap + bow
    return str(ribbon)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
