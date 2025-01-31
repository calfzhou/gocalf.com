class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        min2 = lambda a, b: a if a <= b else b
        n = len(s)
        arr = list(s)
        for i in range(0, len(arr), k << 1):
            l = i
            r = min2(i + k - 1, n - 1)
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        return ''.join(arr)
