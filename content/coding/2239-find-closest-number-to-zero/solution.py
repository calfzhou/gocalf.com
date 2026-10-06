class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        res = nums[0]
        dist = abs(nums[0])
        for num in nums:
            if abs(num) < dist:
                res = num
                dist = abs(num)
            elif abs(num) == dist and num > res:
                res = num

        return res
