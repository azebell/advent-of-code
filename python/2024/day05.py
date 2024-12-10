from aoc import run_solver


def is_correct(update, rules):
    for i in reversed(range(len(update))):
        for j in reversed(range(i)):
            if update[j] in rules.get(update[i], []):
                return False
    return True

def part1(input_str: str) -> str:
    rules, updates = input_str.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.strip().split("\n")]
    updates = [update.split(",") for update in updates.strip().split("\n")]

    before = dict()
    for prev, next in rules:
        l = before.get(prev, [])
        l.append(next)
        before[prev] = l

    answer = 0
    for update in updates:
        if is_correct(update, before):
            middle = update[(len(update) - 1)//2]
            answer += int(middle)
    return str(answer)

def bubble_swap(update, rules):
    for i in reversed(range(len(update))):
        for j in reversed(range(i)):
            if update[j] in rules.get(update[i], []):
                update[i], update[j] = update[j], update[i]
    return update

def part2(input_str: str) -> str:
    rules, updates = input_str.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.strip().split("\n")]
    updates = [update.split(",") for update in updates.strip().split("\n")]

    before = dict()
    for prev, next in rules:
        l = before.get(prev, [])
        l.append(next)
        before[prev] = l

    answer = 0
    for update in updates:
        if is_correct(update, before):
            continue
        update = bubble_swap(update, before)
        middle = update[(len(update) - 1)//2]
        answer += int(middle)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
