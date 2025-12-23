class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        candidates = set(range(n + 1))
        for num in nums:
            candidates.discard(int(num, 2))

        return format(candidates.pop(), f'0{n}b')
