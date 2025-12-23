from math import ceil

LIMIT = 31622 + 1
counts = [0] * LIMIT
primes = [2]

def is_prime(x: int) -> bool:
    sqrt_x = int(x ** 0.5)
    for p in primes:
        if p > sqrt_x:
            primes.append(x)
            return True
        if x % p == 0:
            return False

counts[2] = 1
for n in range(3, LIMIT):
    counts[n] = counts[n-1]
    if n & 1 and is_prime(n):
        counts[n] += 1


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        total = r - l + 1
        l = ceil(l ** 0.5)
        r = int(r ** 0.5)

        cnt_l = counts[l-1]
        cnt_r = counts[r]
        return total - (cnt_r - cnt_l)
