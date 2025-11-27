import unittest
from hash_table_chaining import HashTableChaining
from hash_functions import hash_djb2

class TestHashTableChaining(unittest.TestCase):
    def test_insert_search_delete(self):
        ht = HashTableChaining(hash_func=hash_djb2)
        ht.insert("apple", 5)
        self.assertEqual(ht.search("apple"), 5)
        ht.delete("apple")
        self.assertIsNone(ht.search("apple"))