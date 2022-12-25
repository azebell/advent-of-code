from aoc import run_solver
from math import lcm


def part1(input_str: str) -> str:
    inp = input_str.strip().splitlines()
    Y, X = len(inp), len(inp[0])
    Z = lcm(Y - 2, X - 2)
    L = {
        (i + j * 1j, {">": 1, "v": 1j, "<": -1, "^": -1j}[v])
        for j, l in enumerate(inp, -1)
        for i, v in enumerate(l, -1)
        if "#" != v != "."
    }

    def isInside(pos):  # True iff not a wall
        ins = 0 < pos.real < X - 1 and 0 < pos.imag < Y - 1
        return ins or pos == 1 or pos == X - 2 + (Y - 1) * 1j

    def blizzardPos(pos, d, n):  # where blizzard at after n steps (in blizzard coords)
        pos += n * d
        return pos.real % (X - 2) + (pos.imag % (Y - 2)) * 1j

    def find(start, end, steps):
        res = -1
        visited = set()
        nmoves = [start]
        while nmoves:
            moves, nmoves = nmoves, []
            S = {
                blizzardPos(pos, d, steps) + 1 + 1j for pos, d in L
            }  # positions occupied by blizzards (in map coords)
            for p in moves:
                if (p, steps % Z) in visited:
                    continue
                visited.add((p, steps % Z))
                if p == end:
                    res, nmoves = steps, []
                    break
                if p not in S:  # we don't run into a blizzard
                    nmoves.append(p)  # we stay
                    nmoves.extend(  # we move
                        [
                            p + dx + dy * 1j
                            for dx in (-1, 0, 1)
                            for dy in (-1, 0, 1)
                            if (dx == 0) != (dy == 0) and isInside(p + dx + dy * 1j)
                        ]
                    )
            steps += 1  # next minute
        return res

    startToEnd = find(1, X - 2 + (Y - 1) * 1j, 0)
    return str(startToEnd)


def part2(input_str: str) -> str:
    inp = input_str.strip().splitlines()
    Y, X = len(inp), len(inp[0])
    Z = lcm(Y - 2, X - 2)
    L = {
        (i + j * 1j, {">": 1, "v": 1j, "<": -1, "^": -1j}[v])
        for j, l in enumerate(inp, -1)
        for i, v in enumerate(l, -1)
        if "#" != v != "."
    }

    def isInside(pos):  # True iff not a wall
        ins = 0 < pos.real < X - 1 and 0 < pos.imag < Y - 1
        return ins or pos == 1 or pos == X - 2 + (Y - 1) * 1j

    def blizzardPos(pos, d, n):  # where blizzard at after n steps (in blizzard coords)
        pos += n * d
        return pos.real % (X - 2) + (pos.imag % (Y - 2)) * 1j

    def find(start, end, steps):
        res = -1
        visited = set()
        nmoves = [start]
        while nmoves:
            moves, nmoves = nmoves, []
            S = {
                blizzardPos(pos, d, steps) + 1 + 1j for pos, d in L
            }  # positions occupied by blizzards (in map coords)
            for p in moves:
                if (p, steps % Z) in visited:
                    continue
                visited.add((p, steps % Z))
                if p == end:
                    res, nmoves = steps, []
                    break
                if p not in S:  # we don't run into a blizzard
                    nmoves.append(p)  # we stay
                    nmoves.extend(  # we move
                        [
                            p + dx + dy * 1j
                            for dx in (-1, 0, 1)
                            for dy in (-1, 0, 1)
                            if (dx == 0) != (dy == 0) and isInside(p + dx + dy * 1j)
                        ]
                    )
            steps += 1  # next minute
        return res

    startToEnd = find(1, X - 2 + (Y - 1) * 1j, 0)
    endToStart = find(X - 2 + (Y - 1) * 1j, 1, startToEnd)
    startToEndAgain = find(1, X - 2 + (Y - 1) * 1j, endToStart)
    return str(startToEndAgain)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
