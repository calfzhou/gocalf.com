class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        special.sort()
        largest = max2(special[0] - bottom, top - special[-1])
        for i in range(len(special) - 1):
            largest = max2(largest, special[i+1] - special[i] - 1)

        return largest
