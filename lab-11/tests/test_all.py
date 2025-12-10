import unittest
from prefix_function import prefix_function
from kmp_search import kmp_search
from z_function import z_function
from string_matching import rabin_karp_search
from tasks.task_check_cyclic_shift import is_cyclic_shift

class TestStringAlgorithms(unittest.TestCase):
    def test_prefix_function(self):
        self.assertEqual(prefix_function("abcabcd"), [0, 0, 0, 1, 2, 3, 0])

    def test_kmp_search(self):
        self.assertEqual(kmp_search("abacabadaba", "aba"), [0, 4, 8])
    
    def test_z_function(self):
        self.assertEqual(z_function("aabxaaz"), [0, 1, 0, 0, 2, 1, 0])

    def test_rabin_karp(self):
        self.assertEqual(rabin_karp_search("abacabadaba", "aba"), [0, 4, 8])

    def test_cyclic_shift(self):
        self.assertTrue(is_cyclic_shift("abcd", "cdab"))
        self.assertFalse(is_cyclic_shift("abcd", "abdc"))