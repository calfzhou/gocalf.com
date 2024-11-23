class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        known = set()
        for v in nums:
            if v in known:
                return True
            known.add(v)

        return False
