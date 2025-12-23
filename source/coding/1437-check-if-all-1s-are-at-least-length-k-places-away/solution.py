class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        edge = -1
        for i, num in enumerate(nums):
            if num == 0: continue
            if i <= edge: return False
            edge = i + k

        return True
