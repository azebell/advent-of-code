from aoc import run_solver


def part1(input_str: str) -> str:
    total = 0
    for sack in input_str.strip().split("\n"):
        left = sack[: len(sack) // 2]
        right = sack[len(sack) // 2 :]
        common = set(left).intersection(set(right))
        item = common.pop()
        if str.islower(item):
            priority = ord(item) - ord("a") + 1
        else:
            priority = ord(item) - ord("A") + 27
        total += priority
    return str(total)


def part2(input_str: str) -> str:
    total = 0
    sacks = input_str.strip().split("\n")
    sack_iter = iter(sacks)
    groups = zip(sack_iter, sack_iter, sack_iter)
    for group in groups:
        a, b, c = group
        common = set(a).intersection(set(b).intersection(set(c)))
        item = common.pop()
        if str.islower(item):
            priority = ord(item) - ord("a") + 1
        else:
            priority = ord(item) - ord("A") + 27
        total += priority
    return str(total)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
