import random

def generate_random(n: int) -> list:
    return [random.randint(1, 10000) for _ in range(n)]

def generate_sorted(n: int) -> list:
    return list(range(1, n + 1))

def generate_reversed(n: int) -> list:
    return list(range(n, 0, -1))

def generate_almost_sorted(n: int, percent_random=5) -> list:
    arr = list(range(1, n + 1))
    swap_count = int(n * percent_random / 100)
    for _ in range(swap_count):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr