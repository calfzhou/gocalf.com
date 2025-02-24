class OrderedStream:

    def __init__(self, n: int):
        self._n = n
        self._store: list[str|None] = [None] * n
        self._ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        idKey -= 1
        self._store[idKey] = value
        if self._ptr != idKey:
            return []

        while self._ptr < self._n and self._store[self._ptr] is not None:
            self._ptr += 1

        return self._store[idKey:self._ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
