from aoc import run_solver


def span(start, end):
    diff = end - start
    direction = 1 if diff > 0 else -1
    end = end + 1 if diff > 0 else end - 1
    for i in range(start, end, direction):
        yield i


def part1(input_str: str) -> str:
    grid = set()

    for line in input_str.strip().splitlines():
        points = line.split(" -> ")
        points = [tuple(map(int, point.split(","))) for point in points]
        curr = points[0]
        for point in points[1:]:
            for x in span(curr[0], point[0]):
                for y in span(curr[1], point[1]):
                    grid.add((x, y))
            curr = point

    max_y = max(grid, key=lambda x: x[1])[1]

    accumulated = 0

    while True:
        x, y = 500, 0
        while y < max_y:
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid.add((x, y))
                accumulated += 1
                break
        else:
            break

    return str(accumulated)


def part2(input_str: str) -> str:
    grid = set()

    for line in input_str.strip().splitlines():
        points = line.split(" -> ")
        points = [tuple(map(int, point.split(","))) for point in points]
        curr = points[0]
        for point in points[1:]:
            for x in span(curr[0], point[0]):
                for y in span(curr[1], point[1]):
                    grid.add((x, y))
            curr = point

    max_y = max(grid, key=lambda x: x[1])[1]
    ground = max_y + 2

    accumulated = 0

    while (500, 0) not in grid:
        x, y = 500, 0
        while y + 1 < ground:
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid.add((x, y))
                accumulated += 1
                break
        else:
            grid.add((x, y))
            accumulated += 1

    return str(accumulated)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
