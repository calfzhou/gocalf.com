class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        horizontalCut.sort(reverse=True)
        horizontalCut.append(0)
        verticalCut.sort(reverse=True)
        verticalCut.append(0)
        cost = 0
        i = j = 0
        for _ in range(m + n - 2):
            if horizontalCut[i] > verticalCut[j]: # Cut THROUGH on the horizontal line.
                cost += horizontalCut[i] * (j + 1)
                i += 1
            else: # Cut THROUGH on the vertical line.
                cost += verticalCut[j] * (i + 1)
                j += 1

        return cost
