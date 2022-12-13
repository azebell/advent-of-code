from aoc import run_solver


def check(left, right, depth=0):
    # tabs = "  " * depth
    # print(tabs + "- Compare", left, "vs", right)
    if isinstance(left, list) and isinstance(right, list):
        z = list(zip(left, right))
        for pair in z:
            correct = check(*pair, depth + 1)
            if correct != None:
                return correct
        if len(z) < len(left) or len(z) < len(right):
            return len(left) < len(right)
        return None  # keep checking
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        return None  # keep checking
    elif isinstance(left, list) and isinstance(right, int):
        return check(left, [right], depth + 1)
    elif isinstance(left, int) and isinstance(right, list):
        return check([left], right, depth + 1)


def part1(input_str: str) -> str:
    pairs = input_str.strip().split("\n\n")

    total = 0

    for index, pair in enumerate(pairs):
        left, right = map(eval, pair.splitlines())
        if check(left, right):
            total += index + 1

    return str(total)


def part2(input_str: str) -> str:
    from functools import cmp_to_key

    lines = input_str.strip().splitlines()
    lines = [eval(line) for line in lines if len(line) > 0]
    lines.append([[2]])
    lines.append([[6]])

    lines.sort(key=cmp_to_key(lambda a, b: -1 if check(a, b) else 1))

    p = lines.index([[2]]) + 1
    q = lines.index([[6]]) + 1

    return str(p * q)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
