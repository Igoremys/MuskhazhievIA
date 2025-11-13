# performance_analysis.py

import timeit
import matplotlib.pyplot as plt
from collections import deque
from linked_list import LinkedList

def measure_insert_start(n):
    """Замер времени вставки n элементов в начало"""
    # Для list
    def test_list():
        lst = []
        for i in range(n):
            lst.insert(0, i)

    # Для LinkedList
    def test_linkedlist():
        ll = LinkedList()
        for i in range(n):
            ll.insert_at_start(i)

    time_list = timeit.timeit(test_list, number=1)
    time_ll = timeit.timeit(test_linkedlist, number=1)
    return time_list, time_ll

def measure_dequeue(n):
    """Замер времени удаления n элементов из начала"""
    def test_list_pop():
        lst = list(range(n))
        for _ in range(n):
            lst.pop(0)

    def test_deque_pop():
        dq = deque(range(n))
        for _ in range(n):
            dq.popleft()

    time_list = timeit.timeit(test_list_pop, number=1)
    time_deque = timeit.timeit(test_deque_pop, number=1)
    return time_list, time_deque

if __name__ == "__main__":
    # === Часть 1: Вставка в начало ===
    sizes = [100, 300, 500, 700, 1000]
    list_times = []
    ll_times = []

    print("Замеры для вставки в начало:")
    for n in sizes:
        t_list, t_ll = measure_insert_start(n)
        list_times.append(t_list)
        ll_times.append(t_ll)
        print(f"N={n}: list={t_list:.4f}s, LinkedList={t_ll:.4f}s")

    # Построение графика
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, list_times, label='list.insert(0)', marker='o')
    plt.plot(sizes, ll_times, label='LinkedList.insert_at_start', marker='s')
    plt.xlabel('Количество элементов (N)')
    plt.ylabel('Время (с)')
    plt.title('Сравнение: вставка в начало')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # === Часть 2: Удаление из начала (list vs deque) ===
    print("\nЗамеры для удаления из начала:")
    deque_times = []
    list_pop_times = []

    for n in sizes:
        t_list, t_deque = measure_dequeue(n)
        list_pop_times.append(t_list)
        deque_times.append(t_deque)
        print(f"N={n}: list.pop(0)={t_list:.4f}s, deque.popleft()={t_deque:.4f}s")

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, list_pop_times, label='list.pop(0)', marker='o')
    plt.plot(sizes, deque_times, label='deque.popleft()', marker='s')
    plt.xlabel('Количество элементов (N)')
    plt.ylabel('Время (с)')
    plt.title('Сравнение: удаление из начала')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()