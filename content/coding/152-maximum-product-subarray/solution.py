from typing import List


def prod(*args):
    res = 1
    did = False
    for v in args:
        if v != 0:
            res *= v
            did = True

    return res if did else 0


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (n := len(nums)) == 1:
            return nums[0]

        # Once there are at least two numbers, the largest product must be >= 0.
        largest = 0

        # [prod(left subarray), first <0 number, prod(mid subarray), last <0 number, prod(right subarray)]
        parts = [0]
        for i in range(n + 1):
            if i >= n or (v := nums[i]) == 0: # End of a non-zero subarray.
                if len(parts) < 5: # Zero or one negative number.
                    largest = max(largest, *parts)
                elif parts[2] >= 0: # Negative numbers' count is even (prod(mid) >= 0).
                    largest = max(largest, prod(*parts))
                else: # Negative numbers' count is odd.
                    largest = max(largest, prod(*parts[:3]), prod(*parts[2:]))

                parts = [0]
            elif v > 0:
                parts[-1] = prod(parts[-1], v)
            else:
                if len(parts) < 5:
                    parts.extend((v, 0))
                else:
                    parts[2] = prod(*parts[2:])
                    parts[3] = v
                    parts[4] = 0

        return largest
