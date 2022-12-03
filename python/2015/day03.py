from aoc import run_solver


def part1(input_str: str) -> str:
    x, y = 0, 0
    atlas = {(0, 0): 1}
    for c in input_str:
        if c == "<":
            x -= 1
        elif c == ">":
            x += 1
        elif c == "v":
            y -= 1
        elif c == "^":
            y += 1
        atlas[(x, y)] = atlas.get((x, y), 0) + 1
    return str(len(atlas.keys()))


def part2(input_str: str) -> str:
    atlas = {(0, 0): 2}

    def deliver(moves):
        x, y = 0, 0
        for c in moves:
            if c == "<":
                x -= 1
            elif c == ">":
                x += 1
            elif c == "v":
                y -= 1
            elif c == "^":
                y += 1
            atlas[(x, y)] = atlas.get((x, y), 0) + 1

    deliver(input_str[::2])  # santa moves
    deliver(input_str[1::2])  # robot moves
    return str(len(atlas.keys()))


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
