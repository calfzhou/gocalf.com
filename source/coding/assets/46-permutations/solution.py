class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack():
            if not remains:
                result.append(path.copy())
                return

            for num in list(remains):
                path.append(num)
                remains.remove(num)
                backtrack()
                path.pop()
                remains.add(num)

        path = []
        remains = set(nums)
        backtrack()
        return result
