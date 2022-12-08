from aoc import run_solver


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    grid = [list(map(int, line)) for line in lines]

    visible = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    def rotate(matrix):
        return [list(row) for row in zip(*matrix[::-1])]

    for _ in range(4):
        for y in range(len(grid)):
            tree_top = -1
            for x in range(len(grid[y])):
                tree = grid[y][x]
                if tree > tree_top:
                    visible[y][x] = 1
                tree_top = max(tree_top, tree)
        grid = rotate(grid)
        visible = rotate(visible)

    total = sum([sum(row) for row in visible])
    return str(total)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    grid = [list(map(int, line)) for line in lines]

    def scenic_score(grid, x, y):
        height = grid[y][x]
        up = look(grid, height, x, y - 1, 0, -1)
        down = look(grid, height, x, y + 1, 0, 1)
        right = look(grid, height, x + 1, y, 1, 0)
        left = look(grid, height, x - 1, y, -1, 0)
        return up * down * right * left

    def look(grid, height, x, y, dx, dy):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        elif grid[y][x] >= height:
            return 1
        elif grid[y][x] < height:
            return 1 + look(grid, height, x + dx, y + dy, dx, dy)

    best = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            best = max(best, scenic_score(grid, x, y))
    return str(best)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
