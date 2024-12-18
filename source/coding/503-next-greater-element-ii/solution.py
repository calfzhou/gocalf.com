class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n

        stack = []
        for _ in range(2):
            for i in range(n - 1, -1, -1):
                val = nums[i]
                while stack and stack[-1] <= val:
                    stack.pop()

                if stack: result[i] = stack[-1]
                stack.append(val) # val is greater than stack[-1].

        return result


Solution().nextGreaterElements([1,2,3,4,3])
