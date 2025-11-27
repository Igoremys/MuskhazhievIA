from hash_functions import hash_simple_sum, hash_djb2

class HashTableOpenAddressing:
    def __init__(self, size=16, hash_func=hash_simple_sum, probing='linear'):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = [False] * size
        self.hash_func = hash_func
        self.probing = probing
        self.count = 0

    def _second_hash(self, key, size):
        # Используем DJB2 как вторую хеш-функцию для двойного хеширования
        return 1 + (hash_djb2(key, size - 1))

    def _probe(self, key, i):
        if self.probing == 'linear':
            return (self.hash_func(key, self.size) + i) % self.size
        elif self.probing == 'double':
            h1 = self.hash_func(key, self.size)
            h2 = self._second_hash(key, self.size)
            return (h1 + i * h2) % self.size
        else:
            raise ValueError("Unsupported probing method")

    def insert(self, key, value):
        if self.count >= int(self.size * 0.7):  # Порог α = 0.7
            raise RuntimeError("Table too full (α ≥ 0.7). Resize not implemented for open addressing in this version.")
        i = 0
        while i < self.size:
            idx = self._probe(key, i)
            if self.keys[idx] is None or self.deleted[idx]:
                self.keys[idx] = key
                self.values[idx] = value
                self.deleted[idx] = False
                self.count += 1
                return
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            i += 1
        raise RuntimeError("Hash table is full")

    def search(self, key):
        i = 0
        while i < self.size:
            idx = self._probe(key, i)
            if self.keys[idx] is None:
                return None
            if not self.deleted[idx] and self.keys[idx] == key:
                return self.values[idx]
            i += 1
        return None

    def delete(self, key):
        i = 0
        while i < self.size:
            idx = self._probe(key, i)
            if self.keys[idx] is None:
                return False
            if not self.deleted[idx] and self.keys[idx] == key:
                self.deleted[idx] = True
                self.count -= 1
                return True
            i += 1
        return False