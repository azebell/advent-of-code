from aoc import run_solver


def part1(input_str: str) -> str:
    sequence = map(int, input_str.strip().splitlines())
    sequence = list(enumerate(sequence))
    s = sequence.copy()

    length = len(sequence)

    for entry in sequence:
        if entry[1] == 0:
            zero_entry = entry
        _, value = entry
        idx = s.index(entry)
        new_idx = (idx + value) % (length - 1)
        s.insert(new_idx, s.pop(idx))

    zero_idx = s.index(zero_entry)

    answer = sum(s[(zero_idx + idx) % length][1] for idx in [1000, 2000, 3000])
    return str(answer)


def part2(input_str: str) -> str:
    decrypt_key = 811589153

    sequence = [decrypt_key * int(x) for x in input_str.strip().splitlines()]
    sequence = list(enumerate(sequence))
    s = sequence.copy()

    length = len(sequence)

    for _ in range(10):
        for entry in sequence:
            if entry[1] == 0:
                zero_entry = entry
            _, value = entry
            idx = s.index(entry)
            new_idx = (idx + value) % (length - 1)
            s.insert(new_idx, s.pop(idx))

    zero_idx = s.index(zero_entry)

    answer = sum(s[(zero_idx + idx) % length][1] for idx in [1000, 2000, 3000])
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
