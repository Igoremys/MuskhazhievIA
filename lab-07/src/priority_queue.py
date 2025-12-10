from heap import Heap

class PriorityQueue:
    def __init__(self, is_min=True):
        self.heap = Heap(is_min=is_min)

    def enqueue(self, item, priority):
        """Добавление элемента с приоритетом (O(log n))"""
        self.heap.insert((priority, item))

    def dequeue(self):
        """Извлечение элемента с наивысшим приоритетом (O(log n))"""
        if not self.heap.heap:
            raise IndexError("Priority queue is empty")
        priority, item = self.heap.extract()
        return item