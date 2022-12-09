from aoc import run_solver


directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def part1(input_str: str) -> str:
    head = (0, 0)
    tail = (0, 0)
    visited = {tail}

    for line in input_str.strip().split("\n"):
        move, steps = line.split()
        dx, dy = directions[move]
        steps = int(steps)
        for _ in range(steps):
            head = (head[0] + dx, head[1] + dy)
            tail = shift_tail(head, tail)
            visited.add(tail)

    return str(len(visited))


def part2(input_str: str) -> str:
    head = (0, 0)
    knots = [(0, 0) for _ in range(9)]
    visited = {(0, 0)}

    for line in input_str.strip().split("\n"):
        move, steps = line.split()
        dx, dy = directions[move]
        steps = int(steps)
        for _ in range(steps):
            head = (head[0] + dx, head[1] + dy)
            curr = head
            for i in range(len(knots)):
                knots[i] = shift_tail(curr, knots[i])
                curr = knots[i]
            visited.add(knots[-1])

    return str(len(visited))


def shift_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    if -1 <= hx - tx <= 1 and -1 <= hy - ty <= 1:
        return tail

    return tx + unit(hx - tx), ty + unit(hy - ty)


def unit(x):
    return -1 if x < 0 else 1 if x > 0 else 0


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
