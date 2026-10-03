class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        return sum(v if v < 10 else -v for v in nums) != 0
