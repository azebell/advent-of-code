from aoc import run_solver
import re


def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            if current[1] >= previous[1]:
                merged[-1] = (previous[0], current[1])
        else:
            merged.append(current)
    return merged


def part1(input_str: str) -> str:
    sensors = []
    for line in input_str.strip().splitlines():
        matches = re.findall(r"-?\d+", line)
        sx, sy, bx, by = map(int, matches)
        reach = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, reach))

    intervals = []

    for x, y, reach in sensors:
        goal = abs(y - 2000000)
        if reach >= goal:
            slack = reach - goal
            left = x - slack
            right = x + slack
            intervals.append((left, right))

    intervals = merge_intervals(intervals)

    total = 0
    for interval in intervals:
        total += interval[1] - interval[0]

    return str(total)


def part2(input_str: str) -> str:
    sensors = []
    for line in input_str.strip().splitlines():
        matches = re.findall(r"-?\d+", line)
        sx, sy, bx, by = map(int, matches)
        reach = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, reach))

    beacon_x, beacon_y = -1, -1
    for row in range(4000000 + 1):
        intervals = []
        for x, y, reach in sensors:
            goal = abs(y - row)
            if reach >= goal:
                slack = reach - goal
                left = x - slack
                right = x + slack
                intervals.append((left, right))

        intervals = merge_intervals(intervals)
        if len(intervals) > 1:
            beacon_x = intervals[0][1] + 1
            beacon_y = row
            break

    return str(beacon_x * 4000000 + beacon_y)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
