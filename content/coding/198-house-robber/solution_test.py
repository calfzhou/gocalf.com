import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),

    ([2,7,9,3,1,1,1,100], 112),
    ([2,7,9,3,1,2], 13),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        nums = list(nums) # sol.rob will modify nums.
        assert sol.rob(nums) == expected

    def test_solution2(self, nums, expected):
        sol = Solution2()
        nums = list(nums) # sol.rob will modify nums.
        assert sol.rob(nums) == expected
