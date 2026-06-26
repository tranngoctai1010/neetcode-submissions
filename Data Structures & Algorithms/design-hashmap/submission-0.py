class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, couple in enumerate(self.table[idx]):
            if couple[0] == key:
                self.table[idx][i] = (key, value)
                return

        self.table[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for couple in self.table[idx]:
            if key == couple[0]:
                return couple[1]

        return -1 

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for couple in self.table[idx]:
            if key == couple[0]:
                self.table[idx].remove(couple)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)