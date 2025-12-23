from collections import defaultdict


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        counts: dict[int, int] = defaultdict(int)
        for num in nums:
            counts[num] += 1

        counts = list(counts.items())
        n = len(counts)
        result = []

        def backtrack(i: int, subset: list[int]) -> None:
            if i == n:
                result.append(subset.copy())
                return

            num, count = counts[i]
            for _ in range(count + 1):
                backtrack(i + 1, subset)
                subset.append(num)

            del subset[-count-1:]

        backtrack(0, [])
        return result
