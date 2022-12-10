from aoc import run_solver


def part1(input_str: str) -> str:
    register_values = simulate(input_str)

    total = 0
    for i, val in enumerate(register_values[19::40]):
        cycle = 20 + i * 40
        signal_strength = cycle * val
        total += signal_strength

    return str(total)


def part2(input_str: str) -> str:
    register_values = simulate(input_str)

    screen = ""
    for cycle, val in enumerate(register_values):
        if cycle % 40 == 0:
            screen += "\n"
        if abs(val - (cycle % 40)) <= 1:
            screen += "#"
        else:
            screen += "."

    return str(screen.strip())


def simulate(program: str) -> list[int]:
    X = 1
    register_values = []
    for line in program.strip().split("\n"):
        instruction, *arg = line.split()
        arg = int(arg[0]) if arg else None

        if instruction == "addx":
            register_values.append(X)
            register_values.append(X)
            X += arg
        else:
            register_values.append(X)

    return register_values


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
