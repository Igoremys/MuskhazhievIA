from collections import deque
from typing import Dict, List, Optional, Tuple
from graph_representation import GraphInterface

def bfs(graph: GraphInterface, start: int) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """
    Обход в ширину.
    Возвращает: (расстояния, родители)
    Сложность: O(V + E)
    """
    distances = {start: 0}
    parents = {start: None}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v, _ in graph.get_neighbors(u):
            if v not in distances:
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)
    return distances, parents


def dfs_recursive(graph: GraphInterface, start: int, visited: set = None, order: list = None):
    """
    Рекурсивный DFS.
    Сложность: O(V + E)
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for v, _ in graph.get_neighbors(start):
        if v not in visited:
            dfs_recursive(graph, v, visited, order)
    return order


def dfs_iterative(graph: GraphInterface, start: int) -> List[int]:
    """
    Итеративный DFS.
    Сложность: O(V + E)
    """
    visited = set()
    stack = [start]
    order = []

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            for v, _ in reversed(graph.get_neighbors(u)):
                if v not in visited:
                    stack.append(v)
    return order