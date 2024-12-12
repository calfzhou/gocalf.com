from heapq import heapify, heapreplace


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-v for v in gifts]
        heapify(gifts)
        for _ in range(k):
            if gifts[0] == -1: break
            heapreplace(gifts, -int((-gifts[0]) ** 0.5))

        return -sum(gifts)
