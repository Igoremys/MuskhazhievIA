def rabin_karp_search(text: str, pattern: str, prime: int = 10**9 + 7, base: int = 256) -> list[int]:
    """
    Поиск подстроки методом Рабина–Карпа.
    Средняя сложность: O(n + m); худший случай: O(n*m), но редко.
    Память: O(1) кроме результата.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []

    # Предвычисление степени
    pow_base = pow(base, m - 1, prime)

    # Хеш паттерна
    pattern_hash = 0
    for ch in pattern:
        pattern_hash = (pattern_hash * base + ord(ch)) % prime

    # Первое окно
    window_hash = 0
    for i in range(m):
        window_hash = (window_hash * base + ord(text[i])) % prime

    matches = []
    if window_hash == pattern_hash and text[:m] == pattern:
        matches.append(0)

    # Скользящее окно
    for i in range(m, n):
        # Убираем старый символ
        window_hash = (window_hash - ord(text[i - m]) * pow_base) % prime
        # Добавляем новый
        window_hash = (window_hash * base + ord(text[i])) % prime
        # Проверка
        if window_hash == pattern_hash and text[i - m + 1:i + 1] == pattern:
            matches.append(i - m + 1)

    return matches