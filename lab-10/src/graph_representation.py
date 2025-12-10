from typing import Dict, List, Set, Optional

class GraphInterface:
    def add_vertex(self, v: int) -> None:
        raise NotImplementedError

    def remove_vertex(self, v: int) -> None:
        raise NotImplementedError

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        raise NotImplementedError

    def remove_edge(self, u: int, v: int) -> None:
        raise NotImplementedError

    def get_neighbors(self, v: int) -> List:
        raise NotImplementedError

    def has_edge(self, u: int, v: int) -> bool:
        raise NotImplementedError


class AdjacencyMatrixGraph(GraphInterface):
    """
    Представление графа через матрицу смежности.
    Память: O(V^2)
    Добавление/удаление ребра: O(1)
    Получение соседей: O(V)
    """
    def __init__(self, size: int = 0, directed: bool = False):
        self.directed = directed
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_vertex(self, v: int) -> None:
        if v >= self.size:
            diff = v + 1 - self.size
            for row in self.matrix:
                row.extend([0] * diff)
            self.matrix.extend([[0] * (self.size + diff) for _ in range(diff)])
            self.size = v + 1

    def remove_vertex(self, v: int) -> None:
        if v >= self.size:
            return
        for row in self.matrix:
            del row[v]
        del self.matrix[v]
        self.size -= 1

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        self.add_vertex(max(u, v))
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        if u < self.size and v < self.size:
            self.matrix[u][v] = 0
            if not self.directed:
                self.matrix[v][u] = 0

    def has_edge(self, u: int, v: int) -> bool:
        return u < self.size and v < self.size and self.matrix[u][v] != 0

    def get_neighbors(self, v: int) -> List[tuple]:
        if v >= self.size:
            return []
        neighbors = []
        for i in range(self.size):
            if self.matrix[v][i] != 0:
                neighbors.append((i, self.matrix[v][i]))
        return neighbors


class AdjacencyListGraph(GraphInterface):
    """
    Представление графа через список смежности.
    Память: O(V + E)
    Добавление ребра: O(1)
    Удаление ребра: O(degree(v))
    Получение соседей: O(degree(v))
    """
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.graph: Dict[int, Dict[int, float]] = {}

    def add_vertex(self, v: int) -> None:
        if v not in self.graph:
            self.graph[v] = {}

    def remove_vertex(self, v: int) -> None:
        if v in self.graph:
            del self.graph[v]
        for neighbors in self.graph.values():
            if v in neighbors:
                del neighbors[v]

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u][v] = weight
        if not self.directed:
            self.graph[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        if u in self.graph and v in self.graph[u]:
            del self.graph[u][v]
        if not self.directed and v in self.graph and u in self.graph[v]:
            del self.graph[v][u]

    def has_edge(self, u: int, v: int) -> bool:
        return u in self.graph and v in self.graph[u]

    def get_neighbors(self, v: int) -> List[tuple]:
        return list(self.graph.get(v, {}).items())