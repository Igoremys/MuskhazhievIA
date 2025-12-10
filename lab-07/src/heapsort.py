from heap import Heap

def heapsort(array):
    """Heapsort с использованием отдельной кучи (O(n log n))"""
    h = Heap(is_min=True)
    h.build_heap(array)
    sorted_list = []
    while h.heap:
        sorted_list.append(h.extract())
    return sorted_list

def heapsort_inplace(array):
    """In-place Heapsort (O(n log n), без доп. памяти под кучу)"""
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break

    # Построение max-heap in-place
    n = len(array)
    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    # Извлечение максимумов в конец
    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        sift_down(0, end - 1)