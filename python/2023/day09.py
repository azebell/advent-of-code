from aoc import run_solver


def solve(line, solver):
    terms = list(map(int, line.split()))
    return solver(terms)

def forwards(diffs):
    if any(diff != 0 for diff in diffs):
        new_diffs = [y - x for x, y in zip(diffs[:-1], diffs[1:])]
        return diffs[-1] + forwards(new_diffs)
    return 0

def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = sum(solve(line, forwards) for line in lines)
    return str(answer)


def backwards(diffs):
    if any(diff != 0 for diff in diffs):
        new_diffs = [y - x for x, y in zip(diffs[:-1], diffs[1:])]
        return diffs[0] - backwards(new_diffs)
    return 0

def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = sum(solve(line, backwards) for line in lines)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
