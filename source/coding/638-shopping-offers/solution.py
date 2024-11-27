class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        good = lambda o: all(a >= b for a, b in zip(needs, o)) and sum(p * c for p, c in zip(price, o)) > o[-1]
        offers = tuple(filter(good, special)) # Useless special offer removed.
        cache: dict[tuple[int], int] = {} # Or leverage functools.cache or functools.lru_cache.
        cache[(0,) * len(price)] = 0

        def min_amt(need: tuple[int]):
            if need in cache:
                return cache[need]

            amt = sum(p * c for p, c in zip(price, need)) # Direct buy.
            for offer in offers:
                remain = tuple(a - b for a, b in zip(need, offer))
                if any(r < 0 for r in remain):
                    continue
                amt = min(amt, offer[-1] + min_amt(remain))

            cache[need] = amt
            return amt

        return min_amt(tuple(needs))
