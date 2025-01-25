class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_nums = sorted(nums)
        grouping: dict[int, int] = {} # num -> group
        group_indices = [0]
        g = 0
        for i, num in enumerate(sorted_nums):
            if num > sorted_nums[i-1] + limit: # sorted_nums[0] <= sorted_nums[-1] < sorted_nums[-1] + limit
                g += 1
                group_indices.append(i)
            grouping[num] = g

        for i in range(len(nums)):
            g = grouping[nums[i]]
            nums[i] = sorted_nums[group_indices[g]]
            group_indices[g] += 1

        return nums
