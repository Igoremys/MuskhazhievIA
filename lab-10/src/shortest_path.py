import heapq
from collections import deque
from typing import Dict, List, Set, Optional, Tuple
from graph_representation import GraphInterface

def find_connected_components(graph: GraphInterface) -> List[Set[int]]:
    """
    Поиск компонент связности в неориентированном графе.
    Сложность: O(V + E)
    """
    visited = set()
    components = []

    for v in list(graph.graph.keys()) if hasattr(graph, 'graph') else range(getattr(graph, 'size', 0)):
        if v not in visited:
            component = set()
            stack = [v]
            while stack:
                u = stack.pop()
                if u not in visited:
                    visited.add(u)
                    component.add(u)
                    for w, _ in graph.get_neighbors(u):
                        if w not in visited:
                            stack.append(w)
            components.append(component)
    return components


def topological_sort(graph: GraphInterface) -> Optional[List[int]]:
    """
    Топологическая сортировка (алгоритм Кана).
    Только для DAG.
    Сложность: O(V + E)
    """
    if not graph.directed:
        raise ValueError("Topological sort requires a directed graph")

    in_degree = {}
    for v in graph.graph:
        in_degree.setdefault(v, 0)
        for u in graph.graph[v]:
            in_degree.setdefault(u, 0)
            in_degree[u] += 1

    queue = deque([v for v in in_degree if in_degree[v] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph.get_neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != len(in_degree):
        return None  # есть цикл
    return topo_order


def dijkstra(graph: GraphInterface, start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Алгоритм Дейкстры.
    Требует неотрицательные веса.
    Сложность: O((V + E) log V)
    """
    distances = {}
    parents = {}
    pq = [(0, start)]
    visited = set()

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        distances[u] = curr_dist
        parents[u] = None if u == start else parents.get(u)

        for v, weight in graph.get_neighbors(u):
            if v not in visited:
                new_dist = curr_dist + weight
                if v not in distances or new_dist < distances.get(v, float('inf')):
                    distances[v] = new_dist
                    parents[v] = u
                    heapq.heappush(pq, (new_dist, v))
    return distances, parents