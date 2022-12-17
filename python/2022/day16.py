from aoc import run_solver
import re
from dataclasses import dataclass


@dataclass
class Valve:
    id: str
    rate: int
    neighbors: list[str]
    opened: bool


def floyd_warshall():
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    pass


def dfs(current, graph, minutes):
    if minutes == 0:
        return 0
    current_flow = sum([valve.rate for _, valve in graph.items() if valve.opened])
    valve = graph[current]
    flows = []
    for neighbor in valve.neighbors:
        flow = dfs(neighbor, graph, minutes - 1)
        flows.append(flow)
    if not valve.opened:
        flow = dfs(current, graph, minutes - 1)
        flows.append(flow)
    return current_flow + max(flows)


def part1(input_str: str) -> str:
    graph = {}
    for line in input_str.strip().splitlines():
        match = re.match(r".* (\w\w) .*rate=(\d+);.*valves? (.*)", line)
        id = match.group(1)
        rate = int(match.group(2))
        neighbors = match.group(3).split(", ")
        valve = Valve(id, rate, neighbors, False)
        graph[valve.id] = valve

    for id, valve in graph.items():
        print(valve)

    return str("UNSOLVED")


def part2(input_str: str) -> str:
    return str("UNSOLVED")


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
