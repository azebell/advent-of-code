from aoc import run_solver


def char_to_num(c):
    decoding = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2,
    }
    return decoding[c]


def decode(encoded_number):
    digits = reversed(list(map(char_to_num, encoded_number)))
    return sum(digit * (5**i) for i, digit in enumerate(digits))


def encode(number):
    if number == 0:
        return "0"
    encoding = "012=-"
    result = ""
    while number > 0:
        result += encoding[number % 5]
        if number > 2:
            number += 2
        number //= 5
    return result[::-1]


def part1(input_str: str) -> str:
    numbers = input_str.strip().splitlines()
    total = sum(decode(number) for number in numbers)
    return encode(total)


def part2(input_str: str) -> str:
    return str("UNSOLVED")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
