from aoc import run_solver

def part1(input_str: str) -> str:
    maps = input_str.strip().split("\n\n")
    seeds = map(int, maps[0].split(": ")[1].split())
    maps = maps[1:]
    for m in maps:
        new_seeds = []
        for s in seeds:
            for conversion in m.split("\n")[1:]:
                dest, src, length = map(int, conversion.split())
                if src <= s < src+length:
                    new_seeds.append(s - src + dest)
                    break
            else:
                new_seeds.append(s)
        seeds = new_seeds

    answer = min(seeds)
    return str(answer)

def pairwise(L):
    it = iter(L)
    return zip(it, it)

def part2(input_str: str) -> str:
    return str("answer")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
