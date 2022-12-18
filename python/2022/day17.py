from aoc import run_solver


rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # -
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],  # +
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # backwards L
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # |
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # #
]


def shifter(x, y):
    return lambda p: (p[0] + x, p[1] + y)


def shift(rock, x, y):
    return list(map(shifter(x, y), rock))


def span(iterable):
    _min = _max = next(iterable)
    for x in iterable:
        if x > _max:
            _max = x
        elif x < _min:
            _min = x
    return _min, _max


def infinite_iter(iterator):
    i = 0
    total = len(iterator)
    while True:
        yield iterator[i]
        i = (i + 1) % total


def part1(input_str: str) -> str:
    gusts = list(input_str.strip())
    gusts = infinite_iter(gusts)

    pile = set([(x, -1) for x in range(7)])
    height = 0

    for i in range(2022):
        rock = rocks[i % 5].copy()
        rock = shift(rock, 2, height + 3)

        settled = False
        while not settled:
            # gust rock
            gust = next(gusts)
            if gust == "<":
                new_rock = shift(rock, -1, 0)
            elif gust == ">":
                new_rock = shift(rock, 1, 0)

            min_x, max_x = span(x for x, _ in new_rock)
            if min_x >= 0 and max_x < 7:
                if not any(p in pile for p in new_rock):
                    rock = new_rock

            # drop rock
            new_rock = shift(rock, 0, -1)
            if not any(p in pile for p in new_rock):
                rock = new_rock
            else:
                settled = True
                pile.update(rock)
                height = max(y for x, y in pile) + 1

    return str(height)


def part2(input_str: str) -> str:
    return str("UNSOLVED")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
