import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, k, multiplier, expected', [
    ([2,1,3,5,6], 5, 2, [8,4,6,5,6]),
    ([1,2], 3, 4, [16,8]),
])
class Test:
    def test_solution(self, nums, k, multiplier, expected):
        sol = Solution()
        assert sol.getFinalState(nums.copy(), k, multiplier) == expected

    def test_solution2(self, nums, k, multiplier, expected):
        sol = Solution2()
        assert sol.getFinalState(nums.copy(), k, multiplier) == expected
