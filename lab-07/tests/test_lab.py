import unittest
from heap import Heap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue
import random

class TestHeap(unittest.TestCase):
    def test_min_heap(self):
        h = Heap(is_min=True)
        for x in [3, 1, 4, 1, 5]:
            h.insert(x)
        self.assertEqual(h.extract(), 1)
        self.assertEqual(h.extract(), 1)

    def test_max_heap(self):
        h = Heap(is_min=False)
        for x in [3, 1, 4, 1, 5]:
            h.insert(x)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 4)

    def test_build_heap(self):
        arr = [4, 10, 3, 5, 1]
        h = Heap(is_min=True)
        h.build_heap(arr)
        self.assertEqual(h.peek(), 1)

class TestHeapsort(unittest.TestCase):
    def test_heapsort(self):
        arr = [3, 1, 4, 1, 5]
        self.assertEqual(heapsort(arr), [1, 1, 3, 4, 5])

    def test_heapsort_inplace(self):
        arr = [3, 1, 4, 1, 5]
        heapsort_inplace(arr)
        self.assertEqual(arr, [1, 1, 3, 4, 5])

class TestPriorityQueue(unittest.TestCase):
    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.enqueue("low", 3)
        pq.enqueue("high", 1)
        pq.enqueue("medium", 2)
        self.assertEqual(pq.dequeue(), "high")
        self.assertEqual(pq.dequeue(), "medium")

if __name__ == "__main__":
    unittest.main()