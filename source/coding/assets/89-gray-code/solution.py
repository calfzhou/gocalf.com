class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        for i in range(n):
            diff = 1 << i
            result.extend(x + diff for x in reversed(result))
        return result
