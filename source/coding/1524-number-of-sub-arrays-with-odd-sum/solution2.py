MOD = 10 ** 9 + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        total = 0
        prev_sum = [0, 0]
        j = 1
        cnt = 1
        for num in arr:
            if num % 2 == 0:
                cnt += 1
            else:
                prev_sum[j] += cnt
                j = 1 - j
                total = (total + prev_sum[j] * cnt) % MOD
                cnt = 1

        prev_sum[j] += cnt
        return (total + prev_sum[1-j] * cnt) % MOD
