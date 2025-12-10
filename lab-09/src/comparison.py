import time
from dynamic_programming import fib_naive, fib_memo, fib_bottom_up

def time_function(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

def compare_fibonacci(n=35):
    print(f"Сравнение вычисления fib({n}):")
    _, t1 = time_function(fib_naive, n)         # Только для n ≤ 35!
    _, t2 = time_function(fib_memo, n)
    _, t3 = time_function(fib_bottom_up, n)
    print(f"Наивный:      {t1:.4f} сек")
    print(f"Мемоизация:   {t2:.6f} сек")
    print(f"Bottom-up:    {t3:.6f} сек")