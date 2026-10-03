class Solution:
    def maximumSum2(self, arr: list[int]) -> int:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b
        ps = largest = arr[0]
        low = 0
        low2 = 0
        for i in range(1, len(arr)):
            low2 = min2(low2, low + arr[i]) # low2(i) = min(low2(i-1), low(i-2) + arr[i])
            low = min2(low, ps) # low(i-1) = min(low(i-2), ps(i-1))
            ps += arr[i] # ps(i) = ps(i-1) + arr[i]
            largest = max2(largest, ps - min2(low, low2)) # dl(i) = ps(i) - low(i-1), dd(i) = ps(i) - low2(i)

        return largest
