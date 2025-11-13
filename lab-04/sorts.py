from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Сортировка пузырьком.
    Время: O(n²) во всех случаях.
    Память: O(1) — сортировка на месте.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Сортировка выбором.
    Время: O(n²) во всех случаях.
    Память: O(1).
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Сортировка вставками.
    Время: O(n²) в среднем и худшем, O(n) в лучшем.
    Память: O(1).
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Сортировка слиянием.
    Время: O(n log n) во всех случаях.
    Память: O(n) — требуется дополнительная память.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Быстрая сортировка.
    Время: O(n log n) в среднем, O(n²) в худшем.
    Память: O(log n) — рекурсивный стек.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)