from aoc import run_solver
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, str]
    test: int
    yes: int
    no: int


def update(old, op, c):
    c = old if c == "old" else int(c)
    if op == "+":
        return old + c
    elif op == "*":
        return old * c
    return 0


def setup_monkeys(text: str) -> list[Monkey]:
    monkeys = []
    for chunk in text.strip().split("\n\n"):
        lines = chunk.split("\n")
        items = map(int, lines[1].split(": ")[1].split(", "))
        items = list(items)
        _, op, c = lines[2].split("= ")[1].split()
        operation = (op, c)
        test = int(lines[3].split()[-1])
        yes = int(lines[4].split()[-1])
        no = int(lines[5].split()[-1])

        m = Monkey(items, operation, test, yes, no)
        monkeys.append(m)
    return monkeys


def part1(input_str: str) -> str:
    monkeys = setup_monkeys(input_str)

    ranks = [0 for _ in monkeys]

    for _ in range(20):
        for id, m in enumerate(monkeys):
            ranks[id] += len(m.items)
            for _ in range(len(m.items)):
                item = m.items.pop(0)
                item = update(item, *m.operation)
                item //= 3
                if item % m.test == 0:
                    monkeys[m.yes].items.append(item)
                else:
                    monkeys[m.no].items.append(item)

    a, b = sorted(ranks)[-2:]
    return str(a * b)


def part2(input_str: str) -> str:
    monkeys = setup_monkeys(input_str)

    ranks = [0 for _ in monkeys]

    mod_prod = 1
    for m in monkeys:
        mod_prod *= m.test

    for _ in range(10000):
        for id, m in enumerate(monkeys):
            ranks[id] += len(m.items)
            for _ in range(len(m.items)):
                item = m.items.pop(0)
                item = update(item, *m.operation)
                item = item % mod_prod
                if item % m.test == 0:
                    monkeys[m.yes].items.append(item)
                else:
                    monkeys[m.no].items.append(item)

    a, b = sorted(ranks)[-2:]
    return str(a * b)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
