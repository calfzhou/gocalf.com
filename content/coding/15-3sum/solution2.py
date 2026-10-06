from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n - 2):
            if (v_i := nums[i]) > 0:
                break
            if i > 0 and v_i == nums[i - 1]:
                continue # Prevent duplication.

            v_j_max = -v_i >> 1
            v_k_min = -(v_i >> 1)
            j = i + 1
            k = n - 1
            while j < k and nums[j] <= v_j_max and nums[k] >= v_k_min:
                if (s := v_i + nums[j] + nums[k]) == 0:
                    triplets.append([v_i, nums[j], nums[k]])
                if s <= 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 # Prevent duplication.
                if s >= 0:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1 # Prevent duplication.

        return triplets
