import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),

    ([1,2,3,0,4,5,0,6], [0,0,0,0,0,0,0,0]),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.productExceptSelf(nums) == expected

    def test_solution2(self, nums, expected):
        sol = Solution2()
        assert sol.productExceptSelf(nums) == expected
