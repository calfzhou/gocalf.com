MOD = 10 ** 9 + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        e = [1, 0] # e[0] = E(0) + E(2) + E(4) + ...; e[1] = E(1) + E(3) + E(5) + ...
        j = 0
        for num in arr:
            if num % 2 == 1: j = 1 - j
            e[j] += 1

        return (e[0] * e[1]) % MOD
