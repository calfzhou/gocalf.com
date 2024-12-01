class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        store: set[int] = set()
        for n in arr:
            if n == 0 and n in store:
                return True
            store.add(n)
        return any(n != 0 and n & 1 == 0 and (n >> 1) in store for n in arr)
