class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = greatest
            if tmp > greatest:
                greatest = tmp

        return arr
