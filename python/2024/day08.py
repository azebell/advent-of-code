from aoc import run_solver


def show(grid):
    [print("".join(line)) for line in grid]

def visit(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col != '.':
                yield (col, x, y)

def part1(input_str: str) -> str:
    grid = [list(line) for line in input_str.strip().split("\n")]
    antinodes = [list('.')*len(grid[0]) for _ in grid]

    maxX, maxY = len(grid), len(grid[0])
    on_map = lambda x, y: 0 <= x < maxX and 0 <= y < maxY
    
    for freq, x1, y1 in visit(grid):
        for other, x2, y2 in visit(grid):
            if other != freq:
                continue
            if x1 == x2 and y1 == y2:
                continue
            dx, dy = x1 - x2, y1 - y2
            x, y = x1 + dx, y1 + dy
            if on_map(x, y):
                antinodes[y][x] = "#"

    answer = sum(row.count("#") for row in antinodes)
    return str(answer)

def part2(input_str: str) -> str:
    grid = [list(line) for line in input_str.strip().split("\n")]
    antinodes = [list('.')*len(grid[0]) for _ in grid]

    maxX, maxY = len(grid), len(grid[0])
    on_map = lambda x, y: 0 <= x < maxX and 0 <= y < maxY
    
    for freq, x1, y1 in visit(grid):
        for other, x2, y2 in visit(grid):
            if other != freq:
                continue
            if x1 == x2 and y1 == y2:
                continue
            dx, dy = x1 - x2, y1 - y2
            x, y = x1, y1
            while on_map(x, y):
                antinodes[y][x] = "#"
                x, y = x + dx, y + dy

    answer = sum(row.count("#") for row in antinodes)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
