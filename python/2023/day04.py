from aoc import run_solver


def part1(input_str: str) -> str:
    answer = 0
    lines = input_str.strip().split("\n")
    for line in lines:
        _, data = line.split(": ")
        winning, held = data.split(" | ")
        winning = list(map(int, winning.split()))
        held = list(map(int, held.split()))
        wins = [h for h in held if h in winning]
        pts = len(wins)
        if pts > 0:
            answer += 2**(pts-1)
    return str(answer)

def memoize(func):
    memo = {}
    def wrapped(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapped

@memoize
def dfs(i):
    global cards
    num_copies = cards[i]
    count = 1
    for j in range(i+1, i+1+num_copies):
        count += dfs(j)
    return count

def part2(input_str: str) -> str:
    global cards
    answer = 0
    lines = input_str.strip().split("\n")
    cards = []
    for line in lines:
        _, data = line.split(": ")
        winning, held = data.split(" | ")
        winning = list(map(int, winning.split()))
        held = list(map(int, held.split()))
        wins = len([h for h in held if h in winning])
        cards.append(wins)

    for i in range(len(cards)):
        answer += dfs(i)
    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
