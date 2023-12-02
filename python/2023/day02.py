from aoc import run_solver
import re
from functools import reduce


def part1(input_str: str) -> str:
    answer = 0
    
    color_max = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    lines = input_str.strip().split("\n")
    for line in lines:
        game, turns = line.split(": ")
        game_id = int(game.split()[1])
        qtys = re.split(", |; ", turns)
        for q in qtys:
            amt, color = q.split()
            amt = int(amt)
            if amt > color_max[color]:
                break
        else:
            answer += game_id

    return str(answer)


def part2(input_str: str) -> str:
    answer = 0

    lines = input_str.strip().split("\n")
    for line in lines:
        _, turns = line.split(": ")
        qtys = re.split(", |; ", turns)
        fewest = {}
        for qty in qtys:
            amt, color = qty.split()
            fewest[color] = max(int(amt), fewest.get(color, 0))
        
        power = reduce(lambda x, y: x*y, fewest.values())
        answer += power

    return str(answer)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
