from aoc import run_solver


# returns the shortest distance from start to all other nodes
def dijkstra(distances, start):
    """Determines shortest distance from starting node to all other nodes."""
    unvisited = {node: None for node in distances}  # using None as +inf
    prev = {node: None for node in distances}
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
                prev[neighbour] = current

        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        if not candidates:
            break
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    return visited, prev


def tracepath(prev, end):
    """Traces backwards from 'end' node and returns path in order."""
    path = [end]
    curr = prev[end]
    while curr:
        path.append(curr)
        curr = prev[curr]
    return path[::-1]


def part1(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    grid = [[c for c in line] for line in lines]

    cols = len(grid[0])
    rows = len(grid)

    all_coords = []
    start = (0, 0)
    end = (0, 0)
    for row in range(rows):
        for col in range(cols):
            all_coords.append((row, col))
            if grid[row][col] == "S":
                start = (row, col)
                grid[row][col] = "a"
            if grid[row][col] == "E":
                end = (row, col)
                grid[row][col] = chr(ord("z") + 1)
            grid[row][col] = ord(grid[row][col])

    graph = {(row, col): {} for row, col in all_coords}

    def reach(row, col):
        altitude = grid[row][col]
        if row - 1 >= 0:
            other = grid[row - 1][col]
            if other - altitude <= 1:
                graph[(row, col)][(row - 1, col)] = 1
        if row + 1 < rows:
            other = grid[row + 1][col]
            if other - altitude <= 1:
                graph[(row, col)][(row + 1, col)] = 1
        if col - 1 >= 0:
            other = grid[row][col - 1]
            if other - altitude <= 1:
                graph[(row, col)][(row, col - 1)] = 1
        if col + 1 < cols:
            other = grid[row][col + 1]
            if other - altitude <= 1:
                graph[(row, col)][(row, col + 1)] = 1

    for row in range(rows):
        for col in range(cols):
            reach(row, col)

    visited, prev = dijkstra(graph, start)
    path = tracepath(prev, end)

    steps = len(path) - 1  # subtract starting point

    # vis_graph = [[chr(col) for col in row] for row in grid]
    # for row, col in path:
    #     vis_graph[row][col] = "."

    # graph_str = ""
    # for row in range(rows):
    #     for col in range(cols):
    #         graph_str += vis_graph[row][col]
    #     graph_str += "\n"
    # print(graph_str)

    return str(steps)


def part2(input_str: str) -> str:
    lines = input_str.strip().splitlines()
    grid = [[c for c in line] for line in lines]

    cols = len(grid[0])
    rows = len(grid)

    all_coords = []
    start = (0, 0)
    end = (0, 0)
    for row in range(rows):
        for col in range(cols):
            all_coords.append((row, col))
            if grid[row][col] == "S":
                start = (row, col)
                grid[row][col] = "a"
            if grid[row][col] == "E":
                end = (row, col)
                grid[row][col] = chr(ord("z") + 1)
            grid[row][col] = ord(grid[row][col])

    graph = {(row, col): {} for row, col in all_coords}

    def reach(row, col):
        altitude = grid[row][col]
        if row - 1 >= 0:
            other = grid[row - 1][col]
            if altitude - other <= 1:
                graph[(row, col)][(row - 1, col)] = 1
        if row + 1 < rows:
            other = grid[row + 1][col]
            if altitude - other <= 1:
                graph[(row, col)][(row + 1, col)] = 1
        if col - 1 >= 0:
            other = grid[row][col - 1]
            if altitude - other <= 1:
                graph[(row, col)][(row, col - 1)] = 1
        if col + 1 < cols:
            other = grid[row][col + 1]
            if altitude - other <= 1:
                graph[(row, col)][(row, col + 1)] = 1

    for row in range(rows):
        for col in range(cols):
            reach(row, col)

    visited, prev = dijkstra(graph, end)

    shortest = 1e10
    for pos, distance in visited.items():
        row, col = pos
        if chr(grid[row][col]) == "a":
            if distance < shortest:
                shortest = distance
                start = pos

    path = tracepath(prev, start)
    steps = len(path) - 1  # subtract starting point

    # vis_graph = [[chr(col) for col in row] for row in grid]
    # for row, col in path:
    #     vis_graph[row][col] = "."

    # graph_str = ""
    # for row in range(rows):
    #     for col in range(cols):
    #         graph_str += vis_graph[row][col]
    #     graph_str += "\n"
    # print(graph_str)

    return str(steps)


if __name__ == "__main__":
    result = run_solver(part1, part2)
    print(result)
