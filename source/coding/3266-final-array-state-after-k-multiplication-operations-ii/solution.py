from heapq import heapify, heappop, heappush, heappushpop
from math import ceil, log10

MOD = 1_000_000_007


# def bi_power(a: int, n: int) -> int:
#     """Calculates x ** n % MOD."""
#     if n == 0: return 1
#     mask = 1
#     n1 = n
#     while n1 := n1 >> 1:
#         mask <<= 1

#     res = a
#     while mask := mask >> 1:
#         res = res * res % MOD
#         if n & mask:
#             res = res * a % MOD

#     return res


def bi_power(a: int, n: int) -> int:
    """Calculates x ** n % MOD."""
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        n >>= 1
        a = a * a % MOD

    return res


def ilog(a: int, b: int) -> int:
    """Calculates int(log(a, b))."""
    p = int(log10(a) / log10(b))
    if b ** (p + 1) <= a:
        p += 1
    return p


def clog(a: int, b: int) -> int:
    """Calculates ceil(log(a, b))."""
    p = ceil(log10(a) / log10(b))
    if b ** (p - 1) > a:
        p -= 1
    return p


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1: return nums

        n = len(nums)
        top = max(nums)
        powers: dict[int, int] = {} # i: ilog(top / nums[i], multiplier)
        t = 0
        for i in range(n):
            p = ilog(top / nums[i], multiplier)
            if p == 0: continue
            t += p
            if t > k: break
            powers[i] = p
        else:
            share, k = divmod(k - t, n)
            for i, p in powers.items():
                nums[i] *= multiplier ** p

            if k > 0:
                heap = [(-nums[i], -i) for i in range(k)] # A max-heap to get the minimal k values.
                heapify(heap)
                for i in range(k, n):
                    heappushpop(heap, (-nums[i], -i))
                for _, i in heap:
                    nums[-i] = nums[-i] * multiplier % MOD

            if share > 0:
                tmp = bi_power(multiplier, share)
                for i in range(n):
                    nums[i] = nums[i] * tmp % MOD

            return nums

        heap = [(v, i) for i, v in enumerate(nums)]
        heapify(heap)
        while k > 0:
            a, i = heappop(heap)
            b, j = heap[0]
            if j > i: b += 1

            p = clog(b / a, multiplier)
            if p > k:
                p = k

            a *= multiplier ** p
            k -= p
            heappush(heap, (a, i))

        result = [0] * n
        for v, i in heap:
            result[i] = v % MOD
        return result
