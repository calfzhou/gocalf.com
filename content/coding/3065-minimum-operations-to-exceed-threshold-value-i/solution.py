class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cnt = 0
        for num in nums:
            if num < k:
                cnt += 1

        return cnt
