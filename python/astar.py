"""
Refer: https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
"""

from typing import Callable, TypeVar

Node = TypeVar("Node")
Distance = TypeVar("Distance")


def reconstruct_path(cameFrom: dict[Node, Node], current: Node) -> list[Node]:
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


# A* finds a path from start to goal.
# h is the heuristic function. heuristic(n) estimates the cost to reach goal from node n.
def A_Star(
    start: Node,
    goal: Node,
    get_neighbors: Callable[[Node], list[Node]],
    get_distance: Callable[[Node, Node], Distance],
    heuristic: Callable[[Node], Distance],
) -> list[Node]:
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = {start}

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    # gScore = map with default value of Infinity
    gScore = {start: 0}

    # For node n, fScore[n] = gScore[n] + heuristic(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    # fScore = map with default value of Infinity
    fScore = {start: heuristic(start)}

    while openSet:
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue.
        # current = the node in openSet having the lowest fScore[] value
        current = min(openSet, key=lambda node: fScore[node])
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in get_neighbors(current):
            # get_distance(current,neighbor) is the weight of the edge from current to neighbor.
            # tentative_gScore is the distance from start to the neighbor through current.
            tentative_gScore = gScore[current] + get_distance(current, neighbor)
            if tentative_gScore < gScore.get(neighbor, float("inf")):
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + heuristic(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)

    # Open set is empty but goal was never reached
    return []
