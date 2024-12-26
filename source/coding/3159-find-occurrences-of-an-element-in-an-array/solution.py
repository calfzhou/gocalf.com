class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        occurs = [i for i, num in enumerate(nums) if num == x]
        freq = len(occurs)
        return [occurs[j-1] if j <= freq else -1 for j in queries]
