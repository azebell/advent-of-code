from aoc import run_solver


def part1(input_str: str) -> str:
    contained = 0
    for pair in input_str.strip().split("\n"):
        left, right = pair.split(",")

        left = tuple(map(int, left.split("-")))
        right = tuple(map(int, right.split("-")))

        if left[0] >= right[0] and left[1] <= right[1]:
            contained += 1
        elif right[0] >= left[0] and right[1] <= left[1]:
            contained += 1

    return str(contained)


def part2(input_str: str) -> str:
    overlap = 0
    for pair in input_str.strip().split("\n"):
        left, right = pair.split(",")

        left = tuple(map(int, left.split("-")))
        right = tuple(map(int, right.split("-")))

        if left[0] <= right[1] and left[1] >= right[0]:
            overlap += 1

    return str(overlap)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
