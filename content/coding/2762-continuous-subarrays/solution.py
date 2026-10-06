from collections import defaultdict


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = 0
        counts = defaultdict(int) # counts[v]: the number of `v`s in current window.
        i = j = 0
        counts[nums[j]] = 1
        while True:
            if max(counts) - min(counts) <= 2:
                j += 1
                cnt += j - i
                if j == n: break

                val = nums[j]
                counts[val] += 1
            else:
                val = nums[i]
                counts[val] -= 1
                if counts[val] == 0: del counts[val]
                i += 1

        return cnt
