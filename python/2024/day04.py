from aoc import run_solver


def search(grid, row, col, dr, dc, remaining):
    if row < 0 or row >= len(grid):
        return 0
    if col < 0 or col >= len(grid[0]):
        return 0
    if grid[row][col] != remaining[0]:
        return 0
    elif len(remaining) == 1:
        return 1
    result = 0
    rest = remaining[1:]
    result += search(grid, row+dr, col+dc, dr, dc, rest)
    return result


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == 'X':
                answer += search(lines, row, col, -1,  0, "XMAS")
                answer += search(lines, row, col,  1,  0, "XMAS")
                answer += search(lines, row, col,  0, -1, "XMAS")
                answer += search(lines, row, col,  0,  1, "XMAS")
                answer += search(lines, row, col, -1, -1, "XMAS")
                answer += search(lines, row, col, -1,  1, "XMAS")
                answer += search(lines, row, col,  1, -1, "XMAS")
                answer += search(lines, row, col,  1,  1, "XMAS")
    return str(answer)

def is_xmas(grid, row, col):
    corners = [
        grid[row-1][col-1],
        grid[row-1][col+1],
        grid[row+1][col-1],
        grid[row+1][col+1],
    ]
    if set(corners) == {"M", "S"}:
        if corners[0] != corners[3] and corners[1] != corners[2]:
            return True
    return False

def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = 0
    for row in range(1, len(lines)-1):
        for col in range(1, len(lines[0])-1):
            if lines[row][col] == 'A':
                if is_xmas(lines, row, col):
                    answer += 1
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
