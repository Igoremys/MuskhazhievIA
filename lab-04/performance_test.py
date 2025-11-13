import timeit
import copy
import sorts
import generate_data
import pandas as pd

# Характеристики ПК (укажи актуальные!)
PC_INFO = "Intel Core i7-12700H, 32 GB RAM, Windows 11, Python 3.11"

SIZES = [100, 1000, 5000, 10000]
DATA_TYPES = {
    "random": generate_data.generate_random,
    "sorted": generate_data.generate_sorted,
    "reversed": generate_data.generate_reversed,
    "almost_sorted": generate_data.generate_almost_sorted,
}

SORT_FUNCS = {
    "Bubble Sort": sorts.bubble_sort,
    "Selection Sort": sorts.selection_sort,
    "Insertion Sort": sorts.insertion_sort,
    "Merge Sort": sorts.merge_sort,
    "Quick Sort": sorts.quick_sort,
}

def time_sort(func, data):
    data_copy = copy.deepcopy(data)
    return timeit.timeit(lambda: func(data_copy), number=1)

def run_benchmarks():
    results = []
    for size in SIZES:
        for data_name, generator in DATA_TYPES.items():
            data = generator(size)
            for sort_name, sort_func in SORT_FUNCS.items():
                try:
                    elapsed = time_sort(sort_func, data)
                    results.append({
                        "size": size,
                        "data_type": data_name,
                        "algorithm": sort_name,
                        "time_sec": elapsed
                    })
                    print(f"{sort_name:15} | {data_name:12} | n={size:5} | {elapsed:.4f} sec")
                except RecursionError:
                    print(f"{sort_name} | {data_name} | n={size} | ❌ RecursionError")
                    results.append({
                        "size": size,
                        "data_type": data_name,
                        "algorithm": sort_name,
                        "time_sec": float('inf')
                    })
    df = pd.DataFrame(results)
    df.to_csv("benchmark_results.csv", index=False)
    return df