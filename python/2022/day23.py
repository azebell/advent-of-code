from aoc import run_solver


def get_bounds(points):
    min_x = min(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    return (min_x, min_y), (max_x, max_y)


def area(p1, p2):
    return abs((1 + p2[0] - p1[0]) * (1 + p2[1] - p1[1]))


def empty_spots(points):
    num_points = len(points)
    r1, r2 = get_bounds(points)
    a = area(r1, r2)
    return a - num_points


def rotate(L):
    return L[1:] + L[:1]


def get_surrounding(point):
    offsets = [
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (1, 0),
        (1, -1),
        (1, 1),
        (0, -1),
        (-1, -1),
        (1, -1),
        (0, 1),
        (-1, 1),
        (1, 1),
    ]
    surrounding = map(shift(point), offsets)
    return list(surrounding)


def shift(offset):
    dx, dy = offset
    return lambda point: (point[0] + dx, point[1] + dy)


def get_new_pos(point, points, scan_dir, scan_move):
    for p in get_surrounding(point):
        if p in points:
            break
    else:  # no points in surrounding 8 spots
        return point

    scan = zip(scan_dir, scan_move)
    for scan_offsets, movement in scan:
        scan_zone = map(shift(point), scan_offsets)
        for p in scan_zone:
            if p in points:
                break
        else:  # no points in scan zone
            return shift(point)(movement)
    return point


def prepared_get_new_pos(points, scan_dir, scan_move):
    return lambda point: get_new_pos(point, points, scan_dir, scan_move)


def part1(input_str: str) -> str:
    elves = []
    for row, line in enumerate(input_str.strip().splitlines()):
        for col, c in enumerate(line):
            if c == "#":
                elves.append((row, col))

    scan_directions = [
        [(-1, 0), (-1, -1), (-1, 1)],  # north
        [(1, 0), (1, -1), (1, 1)],  # south
        [(0, -1), (-1, -1), (1, -1)],  # west
        [(0, 1), (-1, 1), (1, 1)],  # east
    ]
    scan_movements = [
        (-1, 0),  # north
        (1, 0),  # south
        (0, -1),  # west
        (0, 1),  # east
    ]

    for _ in range(10):
        new_elves = list(
            map(prepared_get_new_pos(elves, scan_directions, scan_movements), elves)
        )

        # turn duplicate positions back to previous positions
        final_elves = new_elves.copy()
        for i, pos in enumerate(new_elves):
            if new_elves.count(pos) > 1:
                final_elves[i] = elves[i]

        elves = final_elves

        # shift scan direction to the next starting spot
        scan_directions = rotate(scan_directions)
        scan_movements = rotate(scan_movements)

    answer = empty_spots(elves)
    return str(answer)


def part2(input_str: str) -> str:
    elves = []
    for row, line in enumerate(input_str.strip().splitlines()):
        for col, c in enumerate(line):
            if c == "#":
                elves.append((row, col))

    scan_directions = [
        [(-1, 0), (-1, -1), (-1, 1)],  # north
        [(1, 0), (1, -1), (1, 1)],  # south
        [(0, -1), (-1, -1), (1, -1)],  # west
        [(0, 1), (-1, 1), (1, 1)],  # east
    ]
    scan_movements = [
        (-1, 0),  # north
        (1, 0),  # south
        (0, -1),  # west
        (0, 1),  # east
    ]

    elves_moved = True
    round = 0
    while elves_moved:
        new_elves = list(
            map(prepared_get_new_pos(elves, scan_directions, scan_movements), elves)
        )

        # turn duplicate positions back to previous positions
        final_elves = new_elves.copy()
        for i, pos in enumerate(new_elves):
            if new_elves.count(pos) > 1:
                final_elves[i] = elves[i]

        elves_moved = any([a != b for a, b in zip(elves, final_elves)])

        elves = final_elves

        # shift scan direction to the next starting spot
        scan_directions = rotate(scan_directions)
        scan_movements = rotate(scan_movements)

        round += 1

    return str(round)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
