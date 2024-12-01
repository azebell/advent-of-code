from aoc import run_solver


def is_safe(levels):
    if all(1 <= (b-a) <= 3 for a, b in zip(levels, levels[1:])):
        return True
    if all(-3 <= (b-a) <= -1 for a, b in zip(levels, levels[1:])):
        return True
    return False

def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe(levels): answer += 1
    return str(answer)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    answer = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            answer += 1
            continue
        else:
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i+1:]):
                    answer += 1
                    break

    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
