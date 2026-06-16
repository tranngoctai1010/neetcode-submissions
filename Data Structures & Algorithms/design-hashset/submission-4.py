class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.items_per_bucket = 1001
        self._set = [None] * self.buckets

    def _hash(self, key):
        return key % self.buckets

    def _pos(self, key):
        return key // self.buckets

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        pos_idx = self._pos(key)

        if self._set[bucket_idx] is None:
            self._set[bucket_idx] = [False] * self.items_per_bucket

        self._set[bucket_idx][pos_idx] = True

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        pos_idx = self._pos(key)

        if self._set[bucket_idx] is not None:
            self._set[bucket_idx][pos_idx] = False

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        pos_idx = self._pos(key)

        if self._set[bucket_idx] is not None:
            return self._set[bucket_idx][pos_idx]
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)