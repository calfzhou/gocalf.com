from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        vals: dict[int, int] = {} # {value: count}
        for v in nums:
            vals[v] = vals.get(v, 0) + 1

        # Triplet: [vi, vj, vk], where vi <= vj <= vk and vi + vj + vk == 0
        triplets: list[list[int]] = []
        for v_i, c_i in vals.items():
            if v_i == 0 and c_i > 2:
                triplets.append([0, 0, 0])
            elif v_i < 0:
                if c_i > 1 and (v_i_double := -v_i << 1) in vals:
                    triplets.append([v_i, v_i, v_i_double])

                v_i_half = -(v_i >> 1) # ceil(-v_i / 2)
                if v_i & 1 == 0 and vals.get(v_i_half, 0) > 1:
                    triplets.append([v_i, v_i_half, v_i_half])

                for v_j in vals:
                    if v_i < v_j < v_i_half and (v_k := -v_i - v_j) in vals:
                        triplets.append([v_i, v_j, v_k])

        return triplets
