import time
from greedy_algorithms import fractional_knapsack, greedy_coin_change, interval_scheduling, huffman_coding, prim_mst, kruskal_mst
from exact_algorithms import exact_knapsack_01

def compare_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    W = 50
    val_frac, _ = fractional_knapsack(items, W)
    val_exact, _ = exact_knapsack_01(items, W)
    print(f"Fractional knapsack (жадный): {val_frac}")
    print(f"0/1 knapsack (точный): {val_exact}")
    # Покажем, что жадный для дробного — оптимален,
    # но если применить его к 0/1 — может быть неоптимален.

def measure_huffman_time():
    import random, string
    sizes = [100, 500, 1000, 5000]
    for n in sizes:
        text = ''.join(random.choices(string.ascii_lowercase, k=n))
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        start = time.time()
        huffman_coding(freq)
        end = time.time()
        print(f"n={n}, time={end - start:.4f}s")

if __name__ == "__main__":
    compare_knapsack()
    measure_huffman_time()