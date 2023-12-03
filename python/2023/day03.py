from aoc import run_solver

def seek(grid, x, y, boundx, boundy):
    if x < 0 or x > boundx: return
    if y < 0 or y > boundy: return
    if not grid[x][y].isdigit(): return 0
    
    number = ""
    while y >= 0 and grid[x][y].isdigit():
        y -= 1
    y += 1
    while y < len(grid[0]) and grid[x][y].isdigit():
        number += grid[x][y]
        grid[x][y] = 'X'
        y += 1
    
    return int(number)


def part1(input_str: str) -> str:
    answer = 0

    grid = [list(line) for line in input_str.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])
    x, y = 0, 0
    while x < rows:
        if not grid[x][y].isdigit() and not grid[x][y].isalpha() and grid[x][y] != '.':
            answer += seek(grid, x-1, y-1, rows, cols)
            answer += seek(grid, x-1, y, rows, cols)
            answer += seek(grid, x-1, y+1, rows, cols)
            answer += seek(grid, x, y-1, rows, cols)
            answer += seek(grid, x, y+1, rows, cols)
            answer += seek(grid, x+1, y-1, rows, cols)
            answer += seek(grid, x+1, y, rows, cols)
            answer += seek(grid, x+1, y+1, rows, cols)
        y += 1
        if y >= cols:
            y = 0
            x += 1

    return str(answer)


def part2(input_str: str) -> str:
    answer = 0

    grid = [list(line) for line in input_str.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])
    x, y = 0, 0
    while x < rows:
        if grid[x][y] == '*':
            numbers = [
                seek(grid, x-1, y-1, rows, cols),
                seek(grid, x-1, y, rows, cols),
                seek(grid, x-1, y+1, rows, cols),
                seek(grid, x, y-1, rows, cols),
                seek(grid, x, y+1, rows, cols),
                seek(grid, x+1, y-1, rows, cols),
                seek(grid, x+1, y, rows, cols),
                seek(grid, x+1, y+1, rows, cols),
            ]
            if numbers.count(0) == 6:
                a, b = [n for n in numbers if n > 0]
                answer += a*b
            
        y += 1
        if y >= cols:
            y = 0
            x += 1

    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
