class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answers = {val: -1 for val in nums1} # {val: val's next greater element}
        stack = []
        for i, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                answers[nums2[stack.pop()]] = val
            stack.append(i)

        for i, val in enumerate(nums1):
            nums1[i] = answers[val]

        return nums1
