import time
import random
import matplotlib.pyplot as plt
from graph_representation import AdjacencyMatrixGraph, AdjacencyListGraph
from graph_traversal import bfs, dfs_iterative
from shortest_path import dijkstra, find_connected_components

def generate_random_graph(n: int, edge_prob: float = 0.01, directed: bool = False, weighted: bool = False):
    """Генерация случайного графа с ~edge_prob * n^2 рёбрами"""
    g_list = AdjacencyListGgraph = AdjacencyListGraph(directed=directed)
    g_matrix = AdjacencyMatrixGraph(n, directed=directed)
    edges = 0
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if random.random() < edge_prob:
                w = random.randint(1, 10) if weighted else 1
                g_list.add_edge(u, v, w)
                g_matrix.add_edge(u, v, w)
                edges += 1
    return g_list, g_matrix, edges


def benchmark_bfs_dfs():
    sizes = [100, 300, 500, 800, 1000]
    times_bfs_list = []
    times_dfs_list = []

    for n in sizes:
        g_list, _, _ = generate_random_graph(n, edge_prob=0.005)
        start = 0

        # BFS
        t0 = time.perf_counter()
        bfs(g_list, start)
        t1 = time.perf_counter()
        times_bfs_list.append(t1 - t0)

        # DFS
        t0 = time.perf_counter()
        dfs_iterative(g_list, start)
        t1 = time.perf_counter()
        times_dfs_list.append(t1 - t0)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_bfs_list, label="BFS (AdjList)", marker='o')
    plt.plot(sizes, times_dfs_list, label="DFS (AdjList)", marker='s')
    plt.xlabel("Количество вершин (V)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Масштабируемость BFS и DFS")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/bfs_dfs_scaling.png")
    plt.show()


def benchmark_dijkstra():
    sizes = [100, 300, 500, 800]
    times = []

    for n in sizes:
        g_list, _, _ = generate_random_graph(n, edge_prob=0.01, directed=True, weighted=True)
        start = 0

        t0 = time.perf_counter()
        dijkstra(g_list, start)
        t1 = time.perf_counter()
        times.append(t1 - t0)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, label="Дейкстра (AdjList)", marker='^', color='green')
    plt.xlabel("Количество вершин (V)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Масштабируемость алгоритма Дейкстры")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/dijkstra_scaling.png")
    plt.show()


def benchmark_representation_add_edge():
    sizes = [100, 300, 500, 800]
    times_list = []
    times_matrix = []

    for n in sizes:
        # Для списка
        g_list = AdjacencyListGraph()
        t0 = time.perf_counter()
        edges = int(0.01 * n * n)
        for _ in range(edges):
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            g_list.add_edge(u, v)
        t1 = time.perf_counter()
        times_list.append(t1 - t0)

        # Для матрицы
        g_matrix = AdjacencyMatrixGraph(n)
        t0 = time.perf_counter()
        for _ in range(edges):
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            g_matrix.add_edge(u, v)
        t1 = time.perf_counter()
        times_matrix.append(t1 - t0)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_list, label="Список смежности", marker='o')
    plt.plot(sizes, times_matrix, label="Матрица смежности", marker='x')
    plt.xlabel("Количество вершин (V)")
    plt.ylabel("Время добавления рёбер (сек)")
    plt.title("Сравнение производительности представлений графа")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/representation_scaling.png")
    plt.show()


if __name__ == "__main__":
    import os
    os.makedirs("images", exist_ok=True)

    print("Запуск бенчмарков и построение графиков...")
    benchmark_bfs_dfs()
    benchmark_dijkstra()
    benchmark_representation_add_edge()
    print("Графики сохранены в папку 'images/'.")