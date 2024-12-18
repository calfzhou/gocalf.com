class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for _ in range(2):
            for i, val in enumerate(nums):
                while stack and nums[stack[-1]] < val:
                    result[stack.pop()] = val
                stack.append(i)

        return result
