from collections import deque
from typing import Dict, Iterable, List, Tuple, TypeVar, Optional

#!/usr/bin/env python3
"""

Simple, reusable BFS utilities for unweighted graphs represented as adjacency maps.

Functions:
- bfs(graph, start): returns (order, parent, distance)
- bfs_shortest_path(graph, start, goal): returns list of nodes for shortest path or [] if none

graph: dict[node, Iterable[node]]
"""

T = TypeVar("T")


def bfs(graph: Dict[T, Iterable[T]], start: T) -> Tuple[List[T], Dict[T, Optional[T]], Dict[T, int]]:
    """
    Perform breadth-first search from `start`.

    Returns:
    - order: list of nodes in the order they were first visited
    - parent: mapping node -> parent node (start has parent None)
    - distance: mapping node -> distance (0 for start)
    """
    if start not in graph:
        raise KeyError("start node not in graph")

    q = deque([start])
    parent: Dict[T, Optional[T]] = {start: None}
    distance: Dict[T, int] = {start: 0}
    order: List[T] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, ()):
            if v not in parent:  # unvisited
                parent[v] = u
                distance[v] = distance[u] + 1
                q.append(v)

    return order, parent, distance


def bfs_shortest_path(graph: Dict[T, Iterable[T]], start: T, goal: T) -> List[T]:
    """
    Return the shortest path from start to goal (inclusive) as a list of nodes.
    If no path exists, return an empty list.
    """
    if start == goal:
        return [start] if start in graph else []

    _, parent, _ = bfs(graph, start)
    if goal not in parent:
        return []

    # reconstruct path
    path: List[T] = []
    cur: Optional[T] = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


if __name__ == "__main__":
    # Example usage
    sample_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    order, parent, distance = bfs(sample_graph, "A")
    print("BFS order:", order)
    print("Parent map:", parent)
    print("Distances:", distance)
    print("Shortest A -> F:", bfs_shortest_path(sample_graph, "A", "F"))