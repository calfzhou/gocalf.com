class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        m = 2 * n - 1
        result = [0] * m
        placed = [False] * (n + 1)

        def backtrack(i: int) -> bool:
            if i == m:
                return True
            elif result[i] != 0:
                return backtrack(i + 1)

            for num in range(n, 0, -1):
                if placed[num]:
                    continue

                pair = i + num if num > 1 else i
                if pair >= m or result[pair] != 0:
                    continue

                placed[num] = True
                result[i] = num
                result[pair] = num
                if backtrack(i + 1):
                    return True
                placed[num] = False
                result[i] = 0
                result[pair] = 0

            return False

        backtrack(0)
        return result
