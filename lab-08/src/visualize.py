import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import time
import random
import string

def plot_huffman_tree(root):
    """
    Визуализирует дерево Хаффмана с использованием networkx и graphviz.
    """
    if root is None:
        print("Дерево пустое")
        return

    G = nx.DiGraph()
    labels = {}
    node_id = 0
    node_map = {}  # сопоставление объектов Node -> уникальный ID

    def assign_ids(node):
        nonlocal node_id
        if node not in node_map:
            node_map[node] = node_id
            if node.char is not None:
                labels[node_id] = f"'{node.char}':{node.freq}"
            else:
                labels[node_id] = str(node.freq)
            node_id += 1
        if node.left:
            assign_ids(node.left)
        if node.right:
            assign_ids(node.right)

    assign_ids(root)

    def add_edges(node):
        if node.left:
            G.add_edge(node_map[node], node_map[node.left])
            add_edges(node.left)
        if node.right:
            G.add_edge(node_map[node], node_map[node.right])
            add_edges(node.right)

    add_edges(root)

    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    except (ImportError, AttributeError):
        # fallback на spring layout, если graphviz не установлен
        pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=1200,
            node_color="lightgreen", font_size=10, font_weight="bold")
    plt.title("Дерево Хаффмана")
    plt.tight_layout()
    plt.show()

def plot_time_complexity():
    """
    Строит график времени выполнения алгоритма Хаффмана
    в зависимости от размера входных данных.
    """
    from greedy_algorithms import huffman_coding

    sizes = [100, 500, 1000, 2000, 5000]
    times = []

    for n in sizes:
        # Генерация случайного текста
        text = ''.join(random.choices(string.ascii_lowercase, k=n))
        freq = defaultdict(int)
        for c in text:
            freq[c] += 1

        start = time.perf_counter()
        huffman_coding(dict(freq))
        end = time.perf_counter()
        times.append(end - start)

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o', color='blue')
    plt.xlabel("Размер входа (символов)")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Зависимость времени работы алгоритма Хаффмана от размера данных")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Пример частот для построения дерева Хаффмана
    freq_example = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}

    try:
        from greedy_algorithms import huffman_coding
        codes, root = huffman_coding(freq_example)
        print("Коды Хаффмана:", codes)

        # Визуализация дерева
        plot_huffman_tree(root)

        # Замер времени и график
        plot_time_complexity()

    except ImportError:
        print("Ошибка: убедитесь, что файл greedy_algorithms.py находится в той же папке.")
    except Exception as e:
        print(f"Ошибка при визуализации: {e}")