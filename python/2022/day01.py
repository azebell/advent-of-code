from aoc import run_solver


def part1(input_str: str) -> str:
    elves = input_str.strip().split("\n\n")
    biggest = 0
    for elf in elves:
        cals = map(int, elf.split("\n"))
        biggest = max(biggest, sum(cals))
    return str(biggest)


def part2(input_str: str) -> str:
    elves = input_str.strip().split("\n\n")
    totals = []
    for elf in elves:
        cals = map(int, elf.split("\n"))
        totals.append(sum(cals))
    totals.sort()
    return str(sum(totals[-3:]))


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
