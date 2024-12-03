from aoc import run_solver


def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    if all(1 <= diff <= 3 for diff in diffs):
        return True
    elif all(-3 <= diff <= -1 for diff in diffs):
        return True
    return False

def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    reports = [list(map(int, line.split())) for line in lines]
    answer = [is_safe(report) for report in reports].count(True)
    return str(answer)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    reports = [list(map(int, line.split())) for line in lines]
    answer = 0
    for report in reports:
        if is_safe(report):
            answer += 1
            continue
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    answer += 1
                    break

    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
