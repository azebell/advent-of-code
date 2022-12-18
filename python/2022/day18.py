from aoc import run_solver
from itertools import combinations


def are_neighbors(a, b):
    distance = sum(abs(p - q) for p, q in zip(a, b))
    return distance == 1


def part1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    voxels = [tuple(map(int, line.split(","))) for line in lines]

    total_surface_area = 6 * len(voxels)

    for a, b in combinations(voxels, 2):
        if are_neighbors(a, b):
            total_surface_area -= 2

    return str(total_surface_area)


def get_neighbors(point, minv, maxv):
    neighbors = set()
    for delta in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        test_point = tuple([d + offset for d, offset in zip(point, delta)])
        if all([d >= minv and d <= maxv for d in test_point]):
            neighbors.add(test_point)
    return neighbors


def part2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    voxels = [tuple(map(int, line.split(","))) for line in lines]
    voxels = set(voxels)

    surface_area = 0
    minv = min(min(voxel) for voxel in voxels) - 1
    maxv = max(max(voxel) for voxel in voxels) + 1
    search_points = [(minv, minv, minv)]
    visited = {search_points[0]}
    while search_points:
        voxel = search_points.pop()
        for neighbor in get_neighbors(voxel, minv, maxv):
            if neighbor in visited:
                continue
            if neighbor in voxels:
                surface_area += 1
            else:
                visited.add(neighbor)
                search_points.append(neighbor)

    return str(surface_area)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
