from aoc import run_solver


def is_valid(test, terms, acc):
    if len(terms) == 0:
        return acc == test
    return is_valid(test, terms[1:], acc + terms[0]) or is_valid(test, terms[1:], acc * terms[0])
        

def part1(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    equations = [line.split(": ") for line in lines]
    answer = 0
    for equation in equations:
        test = int(equation[0])
        terms = list(map(int, equation[1].split()))
        if is_valid(test, terms[1:], terms[0]):
            answer += test
    return str(answer)

def is_valid_2(test, terms, acc):
    if len(terms) == 0:
        return acc == test
    return any([
        is_valid_2(test, terms[1:], acc + terms[0]),
        is_valid_2(test, terms[1:], acc * terms[0]),
        is_valid_2(test, terms[1:], int(f"{acc}{terms[0]}"))
    ])

def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    equations = [line.split(": ") for line in lines]
    answer = 0
    for equation in equations:
        test = int(equation[0])
        terms = list(map(int, equation[1].split()))
        if is_valid_2(test, terms[1:], terms[0]):
            answer += test
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
