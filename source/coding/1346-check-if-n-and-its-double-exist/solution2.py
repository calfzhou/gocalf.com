class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        store: set[int] = set()
        for n in arr:
            if (n & 1 == 0 and (n >> 1) in store) or (n << 1) in store:
                return True
            store.add(n)

        return False
