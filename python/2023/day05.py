from aoc import run_solver

class RangeMap:
    def __init__(self, text):
        self.dest, self.source, self.length = map(int, text.split())
    
    def contains(self, n):
        if n < self.source: return False
        if n >= self.source + self.length: return False
        return True

    def transform(self, n):
        if not self.contains(n): return n
        return n - self.source + self.dest

class Conversion:
    def __init__(self, text):
        title, ranges = text.split(":\n")
        name = title.split()[0]
        self.source_name, self.dest_name = name.split("-to-")
        self.ranges = [RangeMap(r) for r in ranges.split("\n")]


def part1(input_str: str) -> str:
    maps = input_str.strip().split("\n\n")
    seeds = maps[0].split(": ")[1]
    maps = maps[1:]
    items = [{"seed": int(n)} for n in seeds.split()]
    conversions = [Conversion(m) for m in maps]
    for conversion in conversions:
        for item in items:
            r = [r for r in conversion.ranges if r.contains(item[conversion.source_name])]
            if r:
                item[conversion.dest_name] = r[0].transform(item[conversion.source_name])
            else:
                item[conversion.dest_name] = item[conversion.source_name]
    answer = min(item["location"] for item in items)
    return str(answer)

def pairwise(L):
    it = iter(L)
    return zip(it, it)

def part2(input_str: str) -> str:
    return str("answer")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
