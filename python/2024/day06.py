from aoc import run_solver
import re
from functools import reduce

def turn(x, y):
    return (y, -x)

def show(grid):
    [print("".join(line)) for line in grid]

def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    grid = [list(line) for line in lines]
    dx, dy = -1, 0
    row, col = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                row, col = (r, c)
                grid[r][c] = "X"

    while 0 <= row+dx < len(grid) and 0 <= col+dy < len(grid[0]):

        if grid[row+dx][col+dy] == "#":
            dx, dy = turn(dx, dy)
        else:
            row, col = row + dx, col + dy
            grid[row][col] = "X"

    answer = sum(line.count("X") for line in grid)    
    return str(answer)


def part2(input_str: str) -> str:
    return ""


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
