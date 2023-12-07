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

def intersect(a1, a2, b1, b2):
    if a2 <= b1 or b2 <= a1:
        return None
    return max(a1, b1), min(a2, b2)

def difference(a1, a2, b1, b2):
    return pairwise(sorted([x for x in [a1, a2, b1, b2] if a1 <= x <= a2]))

def part2(input_str: str) -> str:
    maps = input_str.strip().split("\n\n")
    intervals = list(pairwise(map(int, maps[0].split(": ")[1].split())))
    maps = maps[1:]
    for m in maps:
        new_intervals = []
        for start, length in intervals:
            for conversion in m.split("\n")[1:]:
                dest, src, length = map(int, conversion.split())
                if src <= start < src+length:
                    chopped_start = start
                    new_start = min(start + length)
                    new_interval = [chopped_start, new_start]
                    new_intervals.append()
                elif src <= start < src+length:
                    new_interval = [0, 0]
                    new_intervals.append()
                
                if length == 0:
                    break
            else:
                new_intervals.append([start, length])
        intervals = new_intervals

    answer = min(intervals)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
