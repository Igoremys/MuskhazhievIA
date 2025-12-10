# plots.py
import matplotlib.pyplot as plt
import random
import string
from kmp_search import kmp_search
from string_matching import rabin_karp_search
import time

def random_string(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def measure_time(algo, text, pattern):
    start = time.perf_counter()
    algo(text, pattern)
    return time.perf_counter() - start

def main():
    sizes = [1000, 5000, 10000, 20000, 50000]  # 5 значений
    kmp_times = []
    rk_times = []

    for n in sizes:
        # Генерируем текст
        text = random_string(n)
        # Берём паттерн из середины текста (гарантированное совпадение)
        pattern = text[n//2 : n//2 + 10] if n >= 10 else text

        # Замеряем KMP
        t_kmp = measure_time(kmp_search, text, pattern)
        kmp_times.append(t_kmp)

        # Замеряем Rabin–Karp
        t_rk = measure_time(rabin_karp_search, text, pattern)
        rk_times.append(t_rk)

    # Построение графика
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, kmp_times, label='KMP', marker='o')
    plt.plot(sizes, rk_times, label='Rabin–Karp', marker='s')
    plt.xlabel('Длина текста (символов)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение времени поиска подстроки')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance_comparison.png')
    plt.show()

if __name__ == '__main__':
    main()