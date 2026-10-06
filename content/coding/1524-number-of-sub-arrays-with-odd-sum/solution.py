MOD = 10 ** 9 + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even_counts: list[int] = []
        cnt = 1
        for num in arr:
            if num % 2 == 0:
                cnt += 1
            else:
                even_counts.append(cnt)
                cnt = 1
        even_counts.append(cnt)

        total = 0
        prev_sum = [0, 0]
        for i in range(len(even_counts) - 1):
            j = i % 2
            prev = even_counts[i]
            prev_sum[j] += prev
            total = (total + prev_sum[j] * even_counts[i+1]) % MOD

        return total
