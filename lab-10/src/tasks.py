from graph_representation import AdjacencyListGraph
from graph_traversal import bfs
from shortest_path import topological_sort, dijkstra

def maze_shortest_path(grid):
    """Задача: кратчайший путь в лабиринте (BFS на сетке)"""
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    g = AdjacencyListGraph()
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 0:
                        g.add_edge((i,j), (ni,nj))
    dist, _ = bfs(g, start)
    return dist.get((rows-1, cols-1), -1)

def is_network_connected(g):
    from shortest_path import find_connected_components
    comps = find_connected_components(g)
    return len(comps) == 1

def task_topo():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    return topological_sort(g)

def task_dijkstra():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("S", "A", 4)
    g.add_edge("S", "B", 2)
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 5)
    g.add_edge("B", "C", 8)
    dist, _ = dijkstra(g, "S")
    return dist["C"]