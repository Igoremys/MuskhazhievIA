import time
from functools import wraps
import matplotlib.pyplot as plt

def count_calls(func):
    """Декоратор для подсчёта количества вызовов функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def fibonacci_memo(n: int, memo: dict = None) -> int:
    """
    Мемоизированная версия вычисления числа Фибоначчи.
    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 0:
        raise ValueError("Число Фибоначчи не определено для отрицательных индексов.")
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci(n: int) -> int:
    """
    Импортировать из recursion.py нельзя без циклической зависимости,
    поэтому дублируем наивную версию здесь для замеров.
    """
    if n < 0:
        raise ValueError("Число Фибоначчи не определено для отрицательных индексов.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def benchmark_and_plot(max_n: int = 35):
    """
    Сравнивает время выполнения наивной и мемоизированной версий
    и строит график зависимости времени от n.
    Выполняет замеры для n = 5, 10, 15, ..., max_n.
    """
    naive_times = []
    memo_times = []
    call_counts = []
    ns = list(range(5, max_n + 1, 5))

    for n in ns:
        # Наивная версия
        start = time.perf_counter()
        naive_res = fibonacci(n)
        naive_time = time.perf_counter() - start

        # Мемоизированная версия
        fibonacci_memo.call_count = 0
        start = time.perf_counter()
        memo_res = fibonacci_memo(n)
        memo_time = time.perf_counter() - start

        # Проверка корректности
        assert naive_res == memo_res, "Результаты не совпадают!"

        naive_times.append(naive_time)
        memo_times.append(memo_time)
        call_counts.append(fibonacci_memo.call_count)

        print(f"n={n}: наивная={naive_time:.4f}с, мемо={memo_time:.6f}с, вызовов={fibonacci_memo.call_count}")

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(ns, naive_times, label="Наивная рекурсия", marker='o')
    plt.plot(ns, memo_times, label="Мемоизация", marker='s')
    plt.xlabel("n (индекс числа Фибоначчи)")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Сравнение времени выполнения: наивная рекурсия vs мемоизация")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Логарифмическая шкала для наглядности
    plt.savefig("fibonacci_comparison.png")
    plt.show()