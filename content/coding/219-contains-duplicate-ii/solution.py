class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        known: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in known and i - known[num] <= k:
                return True
            known[num] = i

        return False
