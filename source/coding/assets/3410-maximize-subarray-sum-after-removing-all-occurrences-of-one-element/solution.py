from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b
        ps = largest = nums[0]
        low = 0
        low2v: dict[int, int] = defaultdict(int)
        low2 = 0
        for i in range(1, len(nums)):
            v = nums[i]
            low2v[v] = min2(low2v[v], low) + v # low2'(v,i) = v + min(low2'(v,j), low(i-2))
            low2 = min2(low2, low2v[v]) # low2(i) = min(low2(i-1), low2'(v,i))
            low = min2(low, ps) # low(i-1) = min(low(i-2), ps(i-1))
            ps += nums[i] # ps(i) = ps(i-1) + arr[i]
            largest = max2(largest, ps - min2(low, low2)) # dl(i) = ps(i) - low(i-1), dd(i) = ps(i) - low2(i)

        return largest
