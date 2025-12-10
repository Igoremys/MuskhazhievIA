class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def _compare(self, a, b):
        return a < b if self.is_min else a > b

    def _sift_up(self, index):
        """Восстановление свойства кучи при вставке (O(log n))"""
        while index > 0:
            parent = (index - 1) // 2
            if not self._compare(self.heap[index], self.heap[parent]):
                break
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def _sift_down(self, index):
        """Восстановление свойства кучи после извлечения (O(log n))"""
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            extremum = index

            if left < n and self._compare(self.heap[left], self.heap[extremum]):
                extremum = left
            if right < n and self._compare(self.heap[right], self.heap[extremum]):
                extremum = right

            if extremum == index:
                break

            self.heap[index], self.heap[extremum] = self.heap[extremum], self.heap[index]
            index = extremum

    def insert(self, value):
        """Вставка элемента (O(log n))"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        """Извлечение корня (O(log n))"""
        if not self.heap:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        """Просмотр корня (O(1))"""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def build_heap(self, array):
        """Построение кучи из массива за O(n)"""
        self.heap = array[:]
        n = len(self.heap)
        for i in range((n - 2) // 2, -1, -1):
            self._sift_down(i)