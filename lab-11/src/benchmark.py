import time
from kmp_search import kmp_search
from string_matching import rabin_karp_search
import random
import string

def random_string(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def benchmark():
    text = random_string(100_000)
    pattern = text[5000:5010]  # реальное вхождение

    # KMP
    start = time.perf_counter()
    kmp_search(text, pattern)
    kmp_time = time.perf_counter() - start

    # Rabin-Karp
    start = time.perf_counter()
    rabin_karp_search(text, pattern)
    rk_time = time.perf_counter() - start

    print(f"KMP: {kmp_time:.4f}s, Rabin-Karp: {rk_time:.4f}s")