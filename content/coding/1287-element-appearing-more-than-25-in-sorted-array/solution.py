from bisect import bisect_left, bisect_right


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        elif n < 8:
            prev = -1
            for num in arr:
                if num == prev:
                    return num
                prev = num

        edges = [n // 4, n // 2, 3 * n // 4]
        # if arr[edges[-1]] == arr[-1]:
        #     return arr[-1]

        min_count = n // 4 + 1
        bi_count = lambda num: bisect_right(arr, num) - bisect_left(arr, num)
        for edge in edges:
            if bi_count(arr[edge]) >= min_count:
                return arr[edge]
