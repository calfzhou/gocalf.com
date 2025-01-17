class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return sum(derived) & 1 == 0
