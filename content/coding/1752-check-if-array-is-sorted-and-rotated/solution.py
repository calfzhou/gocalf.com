class Solution:
    def check(self, nums: list[int]) -> bool:
        prev = nums[-1]
        down = 0
        for num in nums:
            if num < prev:
                down += 1
                if down > 1:
                    return False
            prev = num

        return True
