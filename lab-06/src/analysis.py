import random
import time
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree

def build_balanced_tree(values):
    bst = BinarySearchTree()
    random.shuffle(values)
    for v in values:
        bst.insert(v)
    return bst

def build_degenerate_tree(values):
    bst = BinarySearchTree()
    for v in sorted(values):  # degenerate — как связный список
        bst.insert(v)
    return bst

def measure_search_time(bst, values, trials=1000):
    total = 0
    for _ in range(trials):
        val = random.choice(values)
        start = time.perf_counter()
        bst.search(val)
        total += time.perf_counter() - start
    return total / trials

def run_analysis():
    sizes = [100, 500, 1000, 2000, 5000]
    balanced_times = []
    degenerate_times = []

    for n in sizes:
        values = list(range(n))
        balanced = build_balanced_tree(values.copy())
        degenerate = build_degenerate_tree(values.copy())

        t_bal = measure_search_time(balanced, values)
        t_deg = measure_search_time(degenerate, values)

        balanced_times.append(t_bal)
        degenerate_times.append(t_deg)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, balanced_times, label='Сбалансированное дерево', marker='o')
    plt.plot(sizes, degenerate_times, label='Вырожденное дерево', marker='x')
    plt.xlabel('Количество элементов')
    plt.ylabel('Среднее время поиска (сек)')
    plt.title('Сравнение времени поиска в BST')
    plt.legend()
    plt.grid(True)
    plt.savefig('search_time_comparison.png')
    plt.show()