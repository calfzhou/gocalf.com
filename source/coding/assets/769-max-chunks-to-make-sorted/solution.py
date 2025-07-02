class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        cnt = 0
        j = -1
        for i in range(len(arr)):
            j = max2(j, arr[i])
            if i == j:
                cnt += 1

        return cnt
