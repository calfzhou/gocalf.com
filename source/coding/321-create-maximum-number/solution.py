def pick_max_sub(nums: list[int], k: int) -> list[int]:
    remain_drop = len(nums) - k
    stack = []
    for num in nums:
        while remain_drop and stack and stack[-1] < num:
            stack.pop()
            remain_drop -= 1

        if len(stack) < k:
            stack.append(num)
        else:
            remain_drop -= 1

    return stack


def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    m = len(nums1)
    n = len(nums2)
    res = [0] * (m + n)
    i = j = 0

    def ge(i:int, j: int) -> bool:
        # return nums1[i:] >= nums2[j:]
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                return True
            elif nums1[i] < nums2[j]:
                return False
            else:
                i += 1
                j += 1

        if i < m: return True
        return False

    while i < m or j < n:
        if ge(i, j):
            res[i+j] = nums1[i]
            i += 1
        else:
            res[i+j] = nums2[j]
            j += 1

    return res


class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b
        m = len(nums1)
        n = len(nums2)
        largest = [0]
        for k1 in range(max2(0, k - n), min2(m, k) + 1):
            k2 = k - k1
            sub1 = pick_max_sub(nums1, k1)
            sub2 = pick_max_sub(nums2, k2)
            res = merge(sub1, sub2)
            if res > largest:
                largest = res

        return largest
