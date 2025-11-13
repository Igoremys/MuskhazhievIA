import os

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Рекурсивный бинарный поиск.
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def list_directory_tree(path: str, prefix: str = "", depth: int = 0, max_depth: int = 100):
    """
    Рекурсивный обход файловой системы с ограничением глубины.
    Возвращает максимальную достигнутую глубину.
    """
    if depth > max_depth:
        print(f"{prefix}... (ограничение глубины)")
        return depth
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(f"{prefix}[Нет доступа]")
        return depth
    max_reached = depth
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{item}")
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            extension = "    " if is_last else "│   "
            sub_depth = list_directory_tree(new_path, prefix + extension, depth + 1, max_depth)
            max_reached = max(max_reached, sub_depth)
    return max_reached


def hanoi(n: int, source='A', target='C', auxiliary='B', moves=None):
    """
    Решение задачи Ханойские башни.
    Выводит последовательность ходов.
    Временная сложность: O(2^n)
    Глубина рекурсии: n
    """
    if moves is None:
        moves = []
    if n == 1:
        move = f"Переместить диск 1 с {source} на {target}"
        print(move)
        moves.append(move)
    else:
        hanoi(n - 1, source, auxiliary, target, moves)
        move = f"Переместить диск {n} с {source} на {target}"
        print(move)
        moves.append(move)
        hanoi(n - 1, auxiliary, target, source, moves)
    return moves