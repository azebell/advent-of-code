from aoc import run_solver
from collections import Counter as hist


def part1(input_str: str) -> str:
    elves = {
        complex(x, y)
        for x, r in enumerate(input_str.strip().splitlines())
        for y, c in enumerate(r)
        if c == "#"
    }

    dirs = (-1, 1, -1j, 1j)
    adjs = dirs + (-1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j)

    for r in range(1, 11):
        plan = lambda e: next(
            (
                e + d
                for d in dirs
                if not any(e + d + d * x in elves for x in (0, 1j, -1j))
                and any(e + a in elves for a in adjs)
            ),
            None,
        )

        plans = hist(map(plan, elves))
        moves = [(e, plan(e)) for e in elves if plans[plan(e)] == 1]

        if not moves:
            print(r)
            break
        src, dst = map(set, zip(*moves))
        elves = elves - src | dst

        dirs = dirs[1:] + dirs[:1]

        if r == 10:
            a, *_, b = sorted(e.real for e in elves)
            c, *_, d = sorted(e.imag for e in elves)
            print((b - a + 1) * (d - c + 1) - len(elves))
            return str((b - a + 1) * (d - c + 1) - len(elves))


def part2(input_str: str) -> str:
    elves = {
        complex(x, y)
        for x, r in enumerate(input_str.strip().splitlines())
        for y, c in enumerate(r)
        if c == "#"
    }

    dirs = (-1, 1, -1j, 1j)
    adjs = dirs + (-1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j)

    for r in range(1, 1_000_000):
        plan = lambda e: next(
            (
                e + d
                for d in dirs
                if not any(e + d + d * x in elves for x in (0, 1j, -1j))
                and any(e + a in elves for a in adjs)
            ),
            None,
        )

        plans = hist(map(plan, elves))
        moves = [(e, plan(e)) for e in elves if plans[plan(e)] == 1]

        if not moves:
            print(r)
            return str(r)
        src, dst = map(set, zip(*moves))
        elves = elves - src | dst

        dirs = dirs[1:] + dirs[:1]


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
