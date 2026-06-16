class MyHashSet:

    def __init__(self):
        self.length = 10000
        self._set = [[] for _ in range(10000)]

    def _hash(self, key):
        return key % self.length

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self._set[idx]:
            self._set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self._set[idx]:
            self._set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        if key in self._set[idx]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)