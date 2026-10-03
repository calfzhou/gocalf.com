class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        counts = [0] * (len(A) + 1)
        res = []
        common = 0
        for pair in zip(A, B):
            for num in pair:
                counts[num] += 1
                if counts[num] == 2:
                    common += 1

            res.append(common)

        return res
