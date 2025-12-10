from collections import defaultdict, deque
import heapq

# 1. Interval Scheduling
def interval_scheduling(intervals):
    """
    Возвращает максимальное количество непересекающихся интервалов.
    Жадный выбор: сортируем по времени окончания.
    Сложность: O(n log n)
    """
    if not intervals:
        return []
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    selected = [intervals_sorted[0]]
    for start, end in intervals_sorted[1:]:
        if start >= selected[-1][1]:
            selected.append((start, end))
    return selected


# 2. Fractional Knapsack
def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight)
    capacity: float
    Возвращает максимальную стоимость и список (item, fraction)
    Сложность: O(n log n)
    """
    items_with_ratio = [(v, w, v / w) for v, w in items]
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    result = []
    for v, w, r in items_with_ratio:
        if capacity == 0:
            break
        take = min(w, capacity)
        total_value += r * take
        result.append(((v, w), take / w))
        capacity -= take
    return total_value, result


# 3. Huffman Coding
class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(freq_dict):
    """
    freq_dict: dict {char: frequency}
    Returns: dict {char: code}, root of Huffman tree
    Сложность: O(n log n), где n = кол-во уникальных символов
    """
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heap[0] if heap else None
    codes = {}

    def dfs(node, prefix=""):
        if node:
            if node.char is not None:
                codes[node.char] = prefix or "0"
            else:
                dfs(node.left, prefix + "0")
                dfs(node.right, prefix + "1")

    dfs(root)
    return codes, root


# 4. Coin Change (жадный, только для канонических систем, напр. [1,2,5,10])
def greedy_coin_change(coins, amount):
    """
    Возвращает минимальное кол-во монет (жадно).
    Работает НЕ для всех систем монет!
    Сложность: O(n) после сортировки (предполагаем, что coins отсортированы по убыванию)
    """
    coins = sorted(coins, reverse=True)
    count = 0
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            result.append(coin)
    return count if amount == 0 else -1  # -1 = невозможно


# 5. Prim's Algorithm (MST)
def prim_mst(graph, start=0):
    """
    graph: adjacency list {u: [(v, weight), ...]}
    Returns: list of edges in MST, total weight
    Сложность: O(E log V)
    """
    visited = set()
    min_heap = [(0, start, None)]  # (weight, node, parent)
    mst_edges = []
    total_weight = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst_edges.append((parent, u, weight))
            total_weight += weight
        for v, w in graph.get(u, []):
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))
    return mst_edges, total_weight


# 6. Kruskal's Algorithm (MST)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal_mst(edges, n):
    """
    edges: list of (u, v, weight)
    n: number of vertices
    Returns: MST edges, total weight
    Сложность: O(E log E)
    """
    edges_sorted = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break
    return mst, total