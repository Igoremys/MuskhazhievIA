def hash_simple_sum(s: str, table_size: int) -> int:
    """Сумма ASCII-кодов символов строки по модулю размера таблицы."""
    return sum(ord(c) for c in s) % table_size


def hash_polynomial(s: str, table_size: int, base: int = 31) -> int:
    """Полиномиальная хеш-функция (роллинг-хеш)."""
    h = 0
    for c in s:
        h = (h * base + ord(c)) % table_size
    return h


def hash_djb2(s: str, table_size: int) -> int:
    """Алгоритм DJB2 — простая, но эффективная хеш-функция."""
    h = 5381
    for c in s:
        h = ((h << 5) + h + ord(c)) % (2**32)
    return h % table_size