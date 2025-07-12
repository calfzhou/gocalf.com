class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(remains: list[int]) -> None:
            if not remains:
                result.append(path.copy())
                return

            for i, num in enumerate(remains):
                if i > 0 and remains[i] == remains[i - 1]:
                    continue
                path.append(num)
                backtrack(remains[:i] + remains[i + 1:])
                path.pop()

        nums.sort()
        path: list[int] = []
        backtrack(nums)
        return result
