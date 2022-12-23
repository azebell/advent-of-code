from aoc import run_solver
import re


def part1(input_str: str) -> str:
    directions = [  # (row, col)
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
    ]

    chart, instructions = input_str.split("\n\n")

    atlas = {}
    for row, line in enumerate(chart.splitlines()):
        for col, c in enumerate(line):
            if c != " ":
                atlas[(row, col)] = c

    search_range = len(chart.splitlines()) * 2

    paces = map(int, re.findall(r"\d+", instructions))
    turns = re.findall(r"[RL]", instructions)

    def walk(steps, heading, position):
        for _ in range(steps):
            row, col = (position[0] + heading[0], position[1] + heading[1])
            cell = atlas.get((row, col), " ")
            while cell == " ":
                row, col = (
                    (row + heading[0]) % search_range,
                    (col + heading[1]) % search_range,
                )
                cell = atlas.get((row, col), " ")
            if cell == "#":
                break
            position = (row, col)
        return position

    direction = 0
    turn = 0
    position = walk(1, directions[0], (0, 0))

    for steps in paces:
        heading = directions[direction]
        position = walk(steps, heading, position)
        if turn < len(turns):
            rotation = 1 if turns[turn] == "R" else -1
            direction = (direction + rotation) % len(directions)
            turn += 1

    row, col = position
    row += 1
    col += 1
    return str(1000 * row + 4 * col + direction)


def part2(input_str: str) -> str:
    return str("UNSOLVED")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
