from aoc import run_solver
import re
from itertools import cycle
import math


def parse(input_str):
    lines = input_str.strip().split("\n")
    directions = lines[0]
    lines = lines[2:]
    nodes = [re.sub("[ =(,)]", " ", line).split() for line in lines]
    return directions, {value: (left, right) for (value, left, right) in nodes}


def steps(start, end_pred, directions, graph):
    steps = 0
    current = start
    for dir in cycle(directions):
        if end_pred(current): break
        current = graph[current][0] if dir == "L" else graph[current][1]
        steps += 1
    
    return steps


def part1(input_str: str) -> str:
    directions, graph = parse(input_str)
    return str(steps("AAA", lambda x: x == "ZZZ", directions, graph))


def part2(input_str: str) -> str:
    directions, graph = parse(input_str)
    starts = [value for value in graph.keys() if value.endswith("A")]
    num_steps = [steps(start, lambda x: x.endswith("Z"), directions, graph) for start in starts]
    min_steps = math.lcm(*num_steps)
    return str(min_steps)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
