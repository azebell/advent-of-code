from aoc import run_solver


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    left = []
    right = []
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()
    answer = sum(abs(r - l) for (r,l) in zip(left, right))
    return str(answer)


def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    left = []
    right = dict()
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right[r] = right.get(r, 0) + 1
    answer = 0
    for num in left:
        sim = num * right.get(num, 0)
        answer += sim
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
