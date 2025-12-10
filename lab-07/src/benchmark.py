import time
import random
from heap import Heap
from heapsort import heapsort, heapsort_inplace
import matplotlib.pyplot as plt

def time_insertions(arr):
    h = Heap()
    start = time.time()
    for x in arr:
        h.insert(x)
    return time.time() - start

def time_build_heap(arr):
    h = Heap()
    start = time.time()
    h.build_heap(arr)
    return time.time() - start

def time_heapsort(arr):
    start = time.time()
    heapsort_inplace(arr.copy())
    return time.time() - start

def time_quicksort(arr):
    start = time.time()
    sorted(arr)  # Python использует Timsort, но для сравнения подойдёт
    return time.time() - start

sizes = [1000, 2000, 5000, 10000, 20000]
insert_times = []
build_times = []
heapsort_times = []
quicksort_times = []

for n in sizes:
    arr = [random.randint(1, 10000) for _ in range(n)]
    insert_times.append(time_insertions(arr))
    build_times.append(time_build_heap(arr))
    heapsort_times.append(time_heapsort(arr))
    quicksort_times.append(time_quicksort(arr))

plt.plot(sizes, insert_times, label="Последовательная вставка (O(n log n))")
plt.plot(sizes, build_times, label="build_heap (O(n))")
plt.plot(sizes, heapsort_times, label="Heapsort")
plt.plot(sizes, quicksort_times, label="Timsort (Python sorted)")
plt.xlabel("Размер массива")
plt.ylabel("Время (сек)")
plt.legend()
plt.title("Сравнение времени работы алгоритмов")
plt.grid(True)
plt.savefig("performance_comparison.png")
plt.show()