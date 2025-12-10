from prefix_function import prefix_function

def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Находит все вхождения pattern в text с помощью алгоритма Кнута-Морриса-Пратта.
    Сложность: O(n + m)
    """
    if not pattern:
        return list(range(len(text) + 1))
    s = pattern + '#' + text  # разделитель гарантирует, что совпадения не пересекут границу
    pi = prefix_function(s)
    matches = []
    pattern_len = len(pattern)
    for i in range(pattern_len + 1, len(s)):
        if pi[i] == pattern_len:
            matches.append(i - 2 * pattern_len)
    return matches