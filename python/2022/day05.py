from aoc import run_solver


def part1(input_str: str) -> str:
    stacks = [[] for _ in range(9)]
    config, moves = input_str.strip().split("\n\n")

    for line in config.split("\n"):
        for i in range(9):
            if 1 + i * 4 >= len(line):
                break
            crate = line[1 + i * 4]
            if crate.isalpha():
                stacks[i].insert(0, crate)

    for move in moves.split("\n"):
        qty, source, dest = map(int, move.split()[1::2])
        for _ in range(qty):
            tmp = stacks[source - 1].pop()
            stacks[dest - 1].append(tmp)

    return "".join([s.pop() for s in stacks])


def part2(input_str: str) -> str:
    stacks = [[] for _ in range(9)]
    config, moves = input_str.strip().split("\n\n")

    for line in config.split("\n"):
        for i in range(9):
            if 1 + i * 4 >= len(line):
                break
            crate = line[1 + i * 4]
            if crate.isalpha():
                stacks[i].insert(0, crate)

    for move in moves.split("\n"):
        qty, source, dest = map(int, move.split()[1::2])
        stacks[dest - 1].extend(stacks[source - 1][-qty:])
        del stacks[source - 1][-qty:]

    return "".join([s.pop() for s in stacks])


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
