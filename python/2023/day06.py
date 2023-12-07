from aoc import run_solver


def part1(input_str: str) -> str:
    answer = 1
    lines = input_str.strip().split("\n")
    times = map(int, lines[0].split()[1:])
    distances = map(int, lines[1].split()[1:])
    for time, distance in zip(times, distances):
        wins = 0
        for held in range(1, time):
            travel_time = time - held
            d = travel_time * held
            if d > distance:
                wins += 1
        answer *= wins
    return str(answer)


def quad_solve(a, b, c):
    p = -b + (b**2 - 4*a*c)**0.5 / 2*a
    q = -b - (b**2 - 4*a*c)**0.5 / 2*a
    return p, q

def part2(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    a, b, c = -1, time, -distance
    l, r = quad_solve(a, b, c)
    return str(int(r) - int(l))

if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
