from hash_functions import hash_simple_sum

class HashTableChaining:
    def __init__(self, initial_size=16, hash_func=hash_simple_sum):
        self.size = initial_size
        self.count = 0
        self.hash_func = hash_func
        self.buckets = [[] for _ in range(self.size)]

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        if self.count >= self.size * 0.75:
            self._resize()
        idx = self.hash_func(key, self.size)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    def search(self, key):
        idx = self.hash_func(key, self.size)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self.hash_func(key, self.size)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False