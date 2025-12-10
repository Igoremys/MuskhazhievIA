import matplotlib.pyplot as plt
from dynamic_programming import knapsack_01
import time

def scalability_test():
    sizes = [10, 20, 30, 40, 50]
    times = []
    for n in sizes:
        weights = list(range(1, n + 1))
        values = list(range(1, n + 1))
        cap = n * 5
        start = time.perf_counter()
        knapsack_01(weights, values, cap)
        times.append(time.perf_counter() - start)
    plt.plot(sizes, times, marker='o')
    plt.title("Scalability of 0-1 Knapsack")
    plt.xlabel("Number of items")
    plt.ylabel("Time (sec)")
    plt.grid()
    plt.savefig("knapsack_time.png")
    plt.show()