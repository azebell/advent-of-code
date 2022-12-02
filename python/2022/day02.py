from aoc import run_solver


def part1(input_str: str) -> str:
    shape_points = [1, 2, 3]

    loss = 0
    draw = 3
    win = 6

    points = 0
    for line in input_str.strip().split("\n"):
        p, q = line.split()
        p = ord(p) - ord("A")
        q = ord(q) - ord("X")

        points += shape_points[q]
        if q - p == 1 or q - p == -2:
            points += win
        elif q - p == 0:
            points += draw
        else:
            points += loss

    return str(points)


def part2(input_str: str) -> str:
    shape_points = [1, 2, 3]

    points = 0
    for line in input_str.strip().split("\n"):
        p, q = line.split()
        p = ord(p) - ord("A")
        q = ord(q) - ord("X")

        points += q * 3
        if q == 0:
            offset = -1
        elif q == 1:
            offset = 0
        else:
            offset = 1
        shape = (p + offset) % 3
        points += shape_points[shape]

    return str(points)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
