from heapq import heappop, heappush


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        min2 = lambda a, b: a if a <= b else b
        store: list[list[int]] = [] # Min-heap of [expiry, count].
        eaten = 0
        for d, cnt in enumerate(apples):
            while store and d >= store[0][0]:
                heappop(store) # Drop rotten apples.

            if apples[d] > 0:
                heappush(store, [d + days[d], apples[d]]) # Save today's new apples in store.

            if store:
                eaten += 1 # Eat an apple which is most likely to rot.
                store[0][1] -= 1
                if store[0][1] == 0:
                    heappop(store)

        d += 1
        while store:
            expiry, cnt = heappop(store)
            if d >= expiry:
                continue # Drop rotten apples.

            cnt = min2(cnt, expiry - d)
            eaten += cnt # Eat all apples which are most likely to rot, before rotten.
            d += cnt

        return eaten
