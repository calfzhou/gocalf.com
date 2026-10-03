class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answers: dict[int, int] = {} # {val: val's next greater element}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            val = nums2[i]
            while stack and stack[-1] < val:
                stack.pop()

            answers[val] = stack[-1] if stack else -1
            stack.append(val) # val is greater than stack[-1].

        for i, val in enumerate(nums1):
            nums1[i] = answers[val]

        return nums1
