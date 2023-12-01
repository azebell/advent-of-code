from aoc import run_solver
import re


def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    values = [re.sub("[^0-9]", "", line) for line in lines]
    values = [f"{value[0]}{value[-1]}" for value in values]
    answer = sum(map(int, values))
    return str(answer)


def part2(input_str: str) -> str:
    numbers = [
        "one", "1",
        "two", "2",
        "three", "3",
        "four", "4",
        "five", "5",
        "six", "6",
        "seven", "7",
        "eight", "8",
        "nine", "9"
    ]

    total = 0
    lines = input_str.strip().split("\n")
    for line in lines:
        first = min((line.index(s), s) for s in numbers if s in line)[1]
        last = max((line.rindex(s), s) for s in numbers if s in line)[1]

        i = numbers.index(first) 
        j = numbers.index(last)
        if i % 2 == 0: first = numbers[i+1]
        if j % 2 == 0: last = numbers[j+1]
        
        total += int(f"{first}{last}")

    return str(total)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
